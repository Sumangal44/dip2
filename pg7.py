#7. convert an rgb image to grayscale and save it as a new file
from PIL import Image
img = Image.open('black-dog.jpg')
gray_img = img.convert('L')
gray_img.show()
gray_img.save("gray_image.jpg")