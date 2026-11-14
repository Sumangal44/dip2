# 4. resize an image  and save it as a new file
from PIL import Image

img = Image.open('dog2.png')
print(img.size)

resized_img = img.resize((200, 200))
resized_img.save("resized_img.png")
img.show()
resized_img.show()
print("resized successfully")
