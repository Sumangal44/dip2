#5. flip an image horizontally and vertically and save it as a new file
from PIL import Image

image = Image.open('black-dog-gray-srgb.png')

horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_flip.save('horizontal_flip.png')

vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical_flip.save('vertical_flip.png')

horizontal_flip.show()
vertical_flip.show()

print("image flipped horizonatl and vertical sccussfully")