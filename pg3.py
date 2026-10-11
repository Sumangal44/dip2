# 4. resize an image  and save it as a new file
from PIL import Image

img = Image.open('black-dog-gray-srgb.png')
print(img.size)

resized_img = img.resize((200, 200))
resized_img.save("resized_img.png")
resized_img.show()
print("resized successfully")
