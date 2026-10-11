#4.rotate an image  and save it as a new file
from PIL import Image

img = Image.open('black-dog-gray-srgb.png')
rotated = img.rotate(-85)
rotated.save("rotated_img.png")
rotated.show()
print("rotated sccuessfully")