#8. convert an rgb image to binary and save it as a new file
from PIL import Image
img = Image.open('black-dog.jpg')  
gray_img = img.convert('L')
threshold = 128
binary_img = gray_img.point(lambda p: 255 if p > threshold else 0, mode='1')
binary_img.save('binary_image.png')
binary_img.show()
print("Image converted to binary successfully")