from msilib.schema import Font
from PIL import Image, ImageDraw, ImageFont
import string
import os
import concat.concat_images as concat

#variables
size = 512
allchar = list(string.ascii_uppercase)
fontname = "arial"
font = ImageFont.truetype(f"{fontname}.ttf", size=size)
image_paths = []

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
    path = f'{fontname}/{allchar.index(char)}.png'
    img.save(path)
    image_paths.append(path)

#init
foldergen(fontname)
for letter in allchar:
    fontgen(letter)


# Get list of image paths


# Create and save image grid
image = concat.concat_images(image_paths, (size, size))
image.save('ImageMatrix.png', 'PNG')