# addition of two graysrascle 
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
img=Image.open('dog1.jpg').convert("L")
arr=np.array(img).astype(np.uint16)
result=arr+50
result=np.clip(result,0,255)
output=Image.fromarray(result.astype(np.uint8))

plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title('original image')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(result,cmap='gray')
plt.title('After addition iamge')
plt.axis('off')

plt.show()