#
# The Python Imaging Library
# $Id$
#
# convert sequence format to GIF animation
#
# history:
#       97-01-03 fl     created
#
# Copyright (c) Secret Labs AB 1997.  All rights reserved.
# Copyright (c) Fredrik Lundh 1997.
#
# See the README file for information on usage and redistribution.
#

#
# For special purposes, you can import this module and call
# the makedelta or compress functions yourself.  For example,
# if you have an application that generates a sequence of
# images, you can convert it to a GIF animation using some-
# thing like the following code:
#
#       import Image
#       import gifmaker
#
#       sequence = []
#
#       # generate sequence
#       for i in range(100):
#           im = <generate image i>
#           sequence.append(im)
#
#       # write GIF animation
#       fp = open("out.gif", "wb")
#       gifmaker.makedelta(fp, sequence)
#       fp.close()
#
# Alternatively, use an iterator to generate the sequence, and
# write data directly to a socket.  Or something...
#

from PIL import Image, ImageChops
import string
import binascii
from PIL.GifImagePlugin import getheader, getdata

# --------------------------------------------------------------------
# sequence iterator

class image_sequence:
    def __init__(self, im):
        self.im = im
    def __getitem__(self, ix):
        try:
            if ix:
                self.im.seek(ix)
            return self.im
        except EOFError:
            raise IndexError # end of sequence

# --------------------------------------------------------------------
# straightforward delta encoding

#Header reconstruction - not finished
def reconstructHeader(im, header):
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


    delay = im.info["duration"]/10
    delayflag = format(delay & 0xff, '04x')
    print delayflag[4:8]
    print delayflag[0:4]
    extensionHeader.append(binascii.unhexlify(delayflag[4:8]+delayflag[0:4]))
    extensionHeader.append(binascii.unhexlify(format(transp & 0xff, '02x')))


    extensionHeader.append(b"\x00")
    print extensionHeader
    print binascii.hexlify(header[1])
    return extensionHeader

def makedelta(fp, sequence, headers):
    """Convert list of image frames to a GIF animation file"""

    frames = 0

    previous = None
    for im in sequence:

        #
        # FIXME: write graphics control block before each frame

        if not previous:

            # global header

            for s in getheader(im)[0]:
                fp.write(s)
            fp.write(b"\x21\xFF\x0B\x4E\x45\x54\x53\x43\x41\x50\x45\x32\x2E\x30\x03\x01\x00\x00\x00") #Application Extension netscape looper

            for s in reconstructHeader(im,headers[frames]) + getdata(im):
                fp.write(s)
        else:

            # delta frame
            delta = ImageChops.subtract_modulo(im, previous)

            bbox = delta.getbbox()

            if bbox:

                # compress difference
                for s in reconstructHeader(im,headers[frames]) + getdata(im.crop(bbox), offset = bbox[:2]):
                    fp.write(s)

            else:
                # FIXME: what should we do in this case?
                pass

        previous = im.copy()

        frames = frames + 1

    fp.write(";")

    return frames

# --------------------------------------------------------------------
# main hack

def compress(infile, outfile):

    # open input image, and force loading of first frame
    im = Image.open(infile)
    im.load()

    # open output file
    fp = open(outfile, "wb")

    seq = image_sequence(im)

    makedelta(fp, seq)

    fp.close()


if __name__ == "__main__":

    import sys

    if len(sys.argv) < 3:
        print "GIFMAKER -- create GIF animations"
        print "Usage: gifmaker infile outfile"
        sys.exit(1)

    compress(sys.argv[1], sys.argv[2])
