from PIL import Image, ImageDraw, ImageFont
import gif_editor
import io
import copy

class signature_controller:


    def createSignatureGif(inpath, outpath):
        gif_editor.gif_editor(inpath, outpath, self.turnImageIntoSignature,self.data).modifyGif()

    def turnImageIntoSignature(image, data):

        image = self.resizeImage(image)
        image = self.drawStats(image)
        return image

    def resizeImage(im):
        size = (468,100)
        return im.resize(size, Image.LANCZOS)

    def drawStats(im, data):

        im = im.convert("RGBA")
        self.drawShip(im, data)
        draw = ImageDraw.Draw(im)
        self.drawText(draw, data)
        im = im.convert("P")

        return im

    def drawShip(im, data):
        overlay = Image.open("C:\Users\Jeff\Documents\git\wows_sigs\signatures\small.png")
        w, h = overlay.size
        w = (int)(w*100.0/h)
        h = 100
        size = w,h
        overlay = overlay.resize(size)
        im.paste(overlay,(0,0),overlay)

    def drawText(draw, data):
        fnt = ImageFont.truetype(r"C:\Users\Jeff\Documents\git\wows_sigs\resources\fonts\BebasNeue.otf", 36)
        draw.text((28,-6),"Tioga060",font=fnt)

        fnt = ImageFont.truetype(r"C:\Users\Jeff\Documents\git\wows_sigs\resources\fonts\BebasNeue.otf", 14)
        draw.rectangle([(0,0),(24,14)],fill=(255, 0, 0))
        draw.rectangle([(0,14),(24,28)],fill=(153, 51, 255))
        draw.text((2,-1),"24%",font=fnt)
        draw.text((2,14),"76%",font=fnt)

        fnt = ImageFont.truetype(r"C:\Users\Jeff\Documents\git\wows_sigs\resources\fonts\BebasNeue.otf", 16)
        draw.text((2,82),"EXP/GAME: 1932",font=fnt)



if __name__ == "__main__":
    createSignatureGif("C:\Users\Jeff\Documents\git\wows_sigs\signatures\input.gif", "C:\Users\Jeff\Documents\git\wows_sigs\signatures\output2.gif", False)
    #createSignatureGif("input.gif", "output2.gif", False)
