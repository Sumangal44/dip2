# 2. open the grayscale image and display its width, height, and total number of pixels
from PIL import Image
img = Image.open('black-dog-gray-srgb.png')
width, height = img.size
total_pixels = width * height
print("width:", width)
print("height:", height)
print("Total number of pixels:", total_pixels)