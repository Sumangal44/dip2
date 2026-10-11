import cv2

img = cv2.imread('black-dog-gray-srgb.png')

# 2. Define crop coordinates (Y first, then X)
# img[y_start:y_end, x_start:x_end]
cropped_img = img[50:250, 100:300]

# 3. Save the cropped image
cv2.imwrite('cropped_image.png', cropped_img)

# 4. Display the result
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image cropped successfully")