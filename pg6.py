#6. convert an image to a numpy array and print the pixel values
from PIL import Image
import numpy as np

img = Image.open('black-dog-gray-srgb.png')
pixel = np.array(img)
print(pixel)