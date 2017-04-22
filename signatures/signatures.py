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

def createSignatureGif(inpath, outpath, stats):
    im = Image.open(inpath)
    size = 468,100
    frames = []

    for i, frame in enumerate(iter_frames(im)):
        frames.append(frame.resize(size, Image.LANCZOS))

    fp = open(outpath, "wb")
    gifmakerCopy.makedelta(fp, frames)
    fp.close()
