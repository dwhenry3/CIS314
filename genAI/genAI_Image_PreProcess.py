#pip install cv2
import cv2
import numpy as np

# Read the image
image = cv2.imread('IMG_1697.jpg')

# Resize the image
resized_image = cv2.resize(image, (224, 224))

# Convert to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Normalize pixel values
normalized_image = blurred_image / 255.0

# Display the image
cv2.imshow('Preprocessed Image', normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()