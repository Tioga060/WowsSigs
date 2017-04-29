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
        try:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            frames.append(imframe)
            headers.append(im.extensionHeader)
            i += 1;
        except EOFError:
            return (frames, headers)


def createSignatureGif(inpath, outpath, stats):
    im = Image.open(inpath)

    size = 468,100
    frames, headers = extractGif(im)

    outFrames = []

    for frame in frames:
        f = frame.resize(size, Image.LANCZOS)
        outFrames.append(applyStatsToImage(im))

    fp = open(outpath, "wb")
    gifmakerCopy.makedelta(fp, outFrames, headers)
    fp.close()

def applyStatsToImage(im):
    im = im.convert("RGBA")
    overlay = Image.open("small.png")
    w, h = overlay.size
    w = (int)(w*100.0/h)
    h = 100
    overlay = overlay.resize((w,h), Image.LANCZOS)
    im = Image.alpha_composite(im, overlay)
    return im


if __name__ == "__main__":
    print "creating signatures"
    createSignatureGif("input.gif", "output2.gif", False)
