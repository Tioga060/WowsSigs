from PIL import Image
import gifmakerCopy
import io
import copy

sequence = []

def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

def extractGif(im):
    i=0
    pallet = False
    frames = []
    headers = []
    while 1:
        im.seek(0)
        imframe = im.copy()
        if i == 0:
            palette = imframe.getpalette()
        else:
            imframe.putpalette(palette)
        frames.append(imframe)
        headers.append(im.extensionHeader)
        print im.extensionHeader
    return (frames, headers)

def createSignatureGif(inpath, outpath, stats):
    im = Image.open(inpath)
    print "finished opening"
    size = 468,100
    frames, headers = extractGif(im)
    print "finished extracting"
    print headers
    outFrames = []

    for frame in frames:
        outFrames.append(frame.resize(size, Image.LANCZOS))

    fp = open(outpath, "wb")
    gifmakerCopy.makedelta(fp, frames, headers)
    fp.close()

if __name__ == "__main__":
    print "creating signatures"
    createSignatureGif("input.gif", "output2.gif", False)
