# Q1

### Code discussion

```python 
from PIL import Image
```
   - Imports the `Image` class from the **Pillow** library.
   - Pillow is commonly used in Python for opening, editing, and saving images.

```python 
img = Image.open('black-dog-gray-srgb.png')
```
   - Opens the image file named `black-dog-gray-srgb.png`.
   - The image must be in the current working directory, or you need to provide its full/relative path.
   - The resulting image object is stored in the variable `img`.

```python
img.show()

```
   - Opens the image using the computer's default image viewer.

# Q2
##  Code Discussion

```python
from PIL import Image
```
- Imports the `Image` module from the Pillow library for image processing.

```python
img = Image.open('black-dog-gray-srgb.png')
```
-  Opens the image file `black-dog-gray-srgb.png` and stores it in the variable `img`.

```python
width, height = img.size
```
-  Gets the image dimensions. The width is stored in `width` and the height is stored in `height`.

```python
total_pixels = width * height
```
-  Calculates the total number of pixels by multiplying the width by the height.

```python
print("Width:", width)
```
-  Displays the width of the image.

```python
print("Height:", height)
```
- Displays the height of the image.

```python
print("Total number of pixels:", total_pixels)
```
- Displays the total number of pixels in the image.

# Q3 
### Code discussion


```python
from PIL import Image
```

- Imports the `Image` module from the Pillow library for image processing.



```py
img = Image.open('black-dog-gray-srgb.png')
```

- Opens the image file named `black-dog-gray-srgb.png` and stores it in the variable `img`.



```py
print(img.size)
```

- Displays the original image dimensions in the format `(width, height)`.


```py
resized_img = img.resize((200, 200))
```

- Resizes the image to a width of 200 pixels and a height of 200 pixels. The resized image is stored in `resized_img`.


```py
resized_img.save("resized_img.png")
```

- Saves the resized image as a new file named `resized_img.png`.



```py 
resized_img.show()
```

- Displays the resized image using the computer's default image viewer.



```py
print("resized successfully")
```

- Prints a success message to indicate that the resizing process has finished.

# Q4

### Code Discussion

```python
from PIL import Image
```

- Imports the `Image` module from the Pillow library for image processing.

```python
img = Image.open('black-dog-gray-srgb.png')
```

- Opens the image file named `black-dog-gray-srgb.png` and stores it in the variable `img`.

```python
rotated = img.rotate(-85)
```

- Rotates the image by **85 degrees clockwise** and stores the rotated image in the variable `rotated`. A negative angle indicates clockwise rotation.

```python
rotated.save("rotated_img.png")
```

- Saves the rotated image as a new file named `rotated_img.png`.

```python
rotated.show()
```

- Displays the rotated image using the computer's default image viewer.

```python
print("rotated sccuessfully")
```

- Prints a success message indicating that the image rotation process has finished.

# Q5

### Code Discussion

```python
from PIL import Image
```

- Imports the `Image` module from the Pillow library for image processing.

```python
image = Image.open('black-dog-gray-srgb.png')
```

- Opens the image file named `black-dog-gray-srgb.png` and stores it in the variable `image`.

```python
horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
```

- Flips the image horizontally, reversing the left and right sides, and stores the result in `horizontal_flip`.

```python
horizontal_flip.save('horizontal_flip.png')
```

- Saves the horizontally flipped image as a new file named `horizontal_flip.png`.

```python
vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
```

- Flips the image vertically, reversing the top and bottom, and stores the result in `vertical_flip`.

```python
vertical_flip.save('vertical_flip.png')
```

- Saves the vertically flipped image as a new file named `vertical_flip.png`.

```python
horizontal_flip.show()
```

- Displays the horizontally flipped image using the computer's default image viewer.

```python
vertical_flip.show()
```

- Displays the vertically flipped image using the computer's default image viewer.

```python
print("image flipped horizontal and vertical sccussfully")
```

- Prints a message indicating that the horizontal and vertical flipping operations have finished.

# Q6

### Code Discussion

```python
from PIL import Image
```

- Imports the `Image` module from the Pillow library for image processing.

```python
import numpy as np
```

- Imports the NumPy library and gives it the alias `np` for numerical and array operations.

```python
img = Image.open('black-dog-gray-srgb.png')
```

- Opens the image file named `black-dog-gray-srgb.png` and stores it in the variable `img`.

```python
pixel = np.array(img)
```

- Converts the image into a NumPy array and stores the pixel values in the variable `pixel`.

```python
print(pixel)
```

- Displays the pixel values of the image as a NumPy array. For a grayscale image, each pixel generally contains an intensity value between 0 and 255.

# Q7

### Code Discussion

```python
from PIL import Image
```

- Imports the `Image` module from the Pillow library for image processing.

```python
img = Image.open('black-dog.jpg')
```

- Opens the RGB image file named `black-dog.jpg` and stores it in the variable `img`.

```python
gray_img = img.convert('L')
```

- Converts the RGB image into a grayscale image using the mode `'L'`, which represents 8-bit grayscale intensity values ranging from 0 to 255.

```python
gray_img.show()
```

- Displays the converted grayscale image using the computer's default image viewer.

```python
gray_img.save("gray_image.jpg")
```

- Saves the grayscale image as a new file named `gray_image.jpg`.

# Q8

### Code Discussion

```python
from PIL import Image
```

- Imports the `Image` module from the Pillow library for image processing.

```python
img = Image.open('black-dog.jpg')
```

- Opens the RGB image file named `black-dog.jpg` and stores it in the variable `img`.

```python
gray_img = img.convert('L')
```

- Converts the RGB image into a grayscale image using the mode `'L'`, which represents intensity values ranging from 0 to 255.

```python
threshold = 128
```

- Sets the threshold value to 128 to classify grayscale pixels as black or white.

```python
binary_img = gray_img.point(lambda p: 255 if p > threshold else 0, mode='1')
```

- Converts the grayscale image into a binary image. Pixels with intensity greater than 128 become white, while the remaining pixels become black. The mode `'1'` represents a 1-bit black-and-white image.

```python
binary_img.save('binary_image.png')
```

- Saves the binary image as a new file named `binary_image.png`.

```python
binary_img.show()
```

- Displays the converted binary image using the computer's default image viewer.

```python
print("Image converted to binary successfully")
```

- Prints a success message indicating that the image conversion process has finished.

# Q9

### Code Discussion

```python
import cv2
```

- Imports the OpenCV library, which is used for image processing and computer vision.

```python
img = cv2.imread('black-dog-gray-srgb.png')
```

- Reads the image file named `black-dog-gray-srgb.png` and stores it in the variable `img`.

```python
cropped_img = img[50:250, 100:300]
```

- Crops a portion of the image using array slicing. The Y-coordinates range from 50 to 250, and the X-coordinates range from 100 to 300. The cropped image has a size of 200 × 200 pixels, provided the original image is large enough.

```python
cv2.imwrite('cropped_image.png', cropped_img)
```

- Saves the cropped image as a new file named `cropped_image.png`.

```python
cv2.imshow('Original Image', img)
```

- Displays the original image in a window titled `Original Image`.

```python
cv2.imshow('Cropped Image', cropped_img)
```

- Displays the cropped portion of the image in a window titled `Cropped Image`.

```python
cv2.waitKey(0)
```

- Waits indefinitely for a keyboard key to be pressed before continuing.

```python
cv2.destroyAllWindows()
```

- Closes all OpenCV image display windows.

```python
print("Image cropped successfully")
```

- Prints a message indicating that the image cropping process has finished.

