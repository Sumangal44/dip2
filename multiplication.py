# addition of two graysrascle
from PIL import Image , ImageChops
import matplotlib.pyplot as plt
img1=Image.open('dog1.jpg').convert("L")
img2=Image.open('dog2.png').convert("L")
img2=img2.resize(img1.size)
result=ImageChops.multiply(img1,img2)
plt.subplot(1,3,1)
plt.imshow(img1,cmap='gray')
plt.title('Image1')
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(img2,cmap='gray')
plt.title('Image2')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(result,cmap='gray')
plt.title('multiplication Result')
plt.axis('off')
plt.show()