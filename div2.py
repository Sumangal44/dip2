# division of two images
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
img1=Image.open('dog1.jpg').convert("L")
img2=Image.open('dog2.png').convert("L")
img2=img2.resize(img1.size)
arr1=np.array(img1).astype(np.float32)
arr2=np.array(img2).astype(np.float32)
arr2[arr2==0]=1
result=(arr1/arr2)*255
result=np.clip(result,0,255)
output=Image.fromarray(result.astype(np.uint8))
plt.figure(figsize=(12,4))
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
plt.title('Division Result')
plt.axis('off')
plt.show()