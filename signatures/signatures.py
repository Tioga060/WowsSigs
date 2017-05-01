from PIL import Image, ImageDraw
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
    #headers = []

    while 1:
        try:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            frames.append(imframe)
            #headers.append(im.extensionHeader)
            i += 1;
        except EOFError:
            return frames#, headers


def createSignatureGif(inpath, outpath, stats):
    im = Image.open(inpath)

    size = 468,100
    frames = extractGif(im)
    palette = False
    outFrames = []
    palette = False

    for frame in frames:
        #frame.putalpha(1)
        frame = frame.resize(size, Image.LANCZOS)
        f = applyStatsToImage(frame)
        #d = ImageDraw.Draw(frame)
        #d.text((0,0),"test",(255,255,255,128))

        f.save("C:\Users\Jeff\Documents\git\wows_sigs\signatures\sets\sest"+str(len(outFrames))+".gif","GIF")
        outFrames.append(f)

    fp = open(outpath, "wb")
    gifmakerCopy.makedelta(fp, outFrames)
    fp.close()

def applyStatsToImage(im):

    im = im.convert("RGBA")
    #palette = im.getpalette()
    overlay = Image.open("C:\Users\Jeff\Documents\git\wows_sigs\signatures\small.png")
    #palette += overlay.convert("P").getpalette()

    #palette += overlay.getpalette()
    w, h = overlay.size
    w = (int)(w*100.0/h)
    h = 100
    size = w,h
    overlay = overlay.resize(size)
    #im = Image.alpha_composite(im, overlay)
    im.paste(overlay,(0,0),overlay)
    #im.save("C:\Users\Jeff\Documents\git\wows_sigs\signatures\sefsdf.png","PNG")
    im = im.convert("P")

    return im


if __name__ == "__main__":
    print "creating signatures"
    createSignatureGif("C:\Users\Jeff\Documents\git\wows_sigs\signatures\input3.gif", "C:\Users\Jeff\Documents\git\wows_sigs\signatures\output2.gif", False)
    #createSignatureGif("input.gif", "output2.gif", False)
