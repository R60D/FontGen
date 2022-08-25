from msilib.schema import Font
from PIL import Image, ImageDraw, ImageFont
import string
import os
#variables
size = 512
allchar = list(string.ascii_uppercase)
fontname = "arial"
font = ImageFont.truetype(f"{fontname}.ttf", size=size)

def foldergen(foldername):
        # Create directory
    try:
        # Create target Directory
        os.mkdir(foldername)
        print("Directory " , foldername ,  " Created ") 
    except FileExistsError:
        print("Directory " , foldername ,  " already exists")
def fontgen(char):
    img = Image.new('RGB', (size, size), color='Black')
    imgDraw = ImageDraw.Draw(img)
    textWidth = imgDraw.textlength(char, font=font)
    xText = (size - textWidth) / 2

    imgDraw.text((xText, 0), char, font=font, fill=(255, 255, 255))

    img.save(f'{fontname}/{allchar.index(char)}.png')

#init
foldergen(fontname)
for letter in allchar:
    fontgen(letter)