#
# gif_editor by Jeff "Tioga060" Hanford
# Used to apply PIL functions to gifs and save results
#

from PIL import Image, ImageChops
from PIL.GifImagePlugin import getheader, getdata
import string
import binascii
import io
import copy


# --------------------------------------------------------------------
# sequence iterator

class gif_editor:
    def __init__(self, inpath, outpath, modFunction, args=None):
        self.inpath = inpath
        self.outpath = outpath
        self.modFunction = modFunction
        self.args = args

    def modifyGif(self):
        outFrames = [self.modFunction(frame, self.args) for frame in gif_decoder(self.inpath).decode()]
        gif_encoder(outFrames).writeGif(self.outpath)


class gif_decoder:
    def __init__(self, inpath):
        self.inpath = inpath
        self.frames = []
        self.numframes = 0

    def decode(self):
        im = Image.open(self.inpath)
        pallet = False
        while 1:
            try:
                im.seek(self.numframes)
                imframe = im.copy()
                if self.numframes == 0:
                    palette = imframe.getpalette()
                else:
                    imframe.putpalette(palette)
                self.frames.append(imframe)
                self.numframes += 1;
            except EOFError:
                return self.frames#, headers

class gif_encoder:
    def __init__(self, frames):
        self.frames = frames

    def writeGif(self, outpath):
        fp = open(outpath, "wb")
        self.makedelta(fp, self.frames)
        fp.close()

    def augmentHeader(self, im):
        '''
        Converts the GIF from 87a to 89a - not sure if this is necessary
        Adds the netscape looping code after the header
        '''
        header = binascii.hexlify(getheader(im)[0][0])
        header = header[:6] + "383961" + header[12:]
        return [binascii.unhexlify(header)] + getheader(im)[0][1:] + [b"\x21\xFF\x0B\x4E\x45\x54\x53\x43\x41\x50\x45\x32\x2E\x30\x03\x01\x00\x00\x00"]

    def createApplicationExtension(self, im):
        '''Creates the GIF application extension header to give each frame its proper delay'''
        extensionHeader = [b"\x21\xF9\x04"]

        #note: not using the served bits or the input flag
        flags = 0b00000000
        transp = 0b00000000
        if "transparency" in im.info:
            flags = flags | 0b00000001
            transp = im.info["transparency"]
        if hasattr(im, "disposal_method"):
            flags = flags | (im.disposal_method<<2)
        extensionHeader.append(binascii.unhexlify(format(flags & 0xff, '02x')))

        #Per Frame Delay
        delay = im.info["duration"]/10
        delayflag = format(delay, '04x')

        #These have to be reversed for some reason
        extensionHeader.append(binascii.unhexlify(delayflag[2:]))
        extensionHeader.append(binascii.unhexlify(delayflag[:2]))

        #transparency data
        extensionHeader.append(binascii.unhexlify(format(transp & 0xff, '02x')))
        extensionHeader.append(b"\x00")
        return extensionHeader

    def modifyFlagsAndAppendCTable(self, im, offset = False):
        '''Creates an extension header for each image to specify that it has a local color table, and inserts that local color table before the image data'''
        imageDescriptor = False
        if(offset):
            imageDescriptor = binascii.hexlify(getdata(im, offset=offset)[0])[:-2]
        else:
            imageDescriptor = binascii.hexlify(getdata(im)[0])[:-2]

        flags = "87" #b10000111 - Use local color table with size 111 (2^8 = 256)
        imageDescriptor+=flags
        newDescriptor = [binascii.unhexlify(imageDescriptor)]
        for val in im.getpalette():
            newDescriptor.append(binascii.unhexlify(format(val & 0xff, '02x')))
        if(offset):
            return newDescriptor + getdata(im, offset=offset)[1:]
        else:
            return newDescriptor + getdata(im)[1:]


    def makedelta(self, fp, sequence):
        """Convert list of image frames to a GIF animation file"""

        frames = 0

        previous = None
        for im in sequence:

            if not previous:

                # global header
                for s in self.augmentHeader(im):
                    fp.write(s)

                #Discard the first frame, it is buggy for whatever reason
                for s in self.createApplicationExtension(im) + self.modifyFlagsAndAppendCTable(im.crop((0,0,im.width, im.height)), (0,0)):
                    fp.write(s)
            else:

                # delta frame
                delta = ImageChops.subtract_modulo(im, previous)

                bbox = delta.getbbox()
                if bbox:
                    # compress difference
                    for s in self.createApplicationExtension(im) + self.modifyFlagsAndAppendCTable(im.crop(bbox), bbox[:2]):
                        fp.write(s)

                else:
                    # FIXME: what should we do in this case?
                    pass

            previous = im.copy()

            frames = frames + 1

        fp.write(";")

        return frames
