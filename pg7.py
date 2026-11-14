#7. convert an rgb image to grayscale and save it as a new file
from PIL import Image
img = Image.open('dog2.png')
gray_img = img.convert('L')
img.show()
gray_img.show()
gray_img.save("gray_image.png")