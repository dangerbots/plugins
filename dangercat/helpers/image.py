import asyncio
import os
try:
    pass
except:
    os.system("pip install colour")
import re
import requests

import PIL.ImageOps
from PIL import Image


# inverting colors...
async def invert_colors(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(endname)


# upside down...
async def flip_image(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.flip(image)
    inverted_imag


# dangercat
