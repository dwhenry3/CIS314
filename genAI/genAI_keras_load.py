# pip install opencv-python
import tensorflow as tf
import cv2
import numpy as np

new_model = tf.keras.models.load_model('my_model.keras')

# Load and preprocess the image
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
    img = cv2.resize(img, (28, 28))  # Resize to 28x28
    img = img.astype("float32") / 255.0  # Normalize
    img = img.reshape(1, 784)  # Reshape to match model input (1D vector of 784)
    return img

# Predict the digit
def predict_digit(image_path):
    processed_img = preprocess_image(image_path)
    prediction = new_model.predict(processed_img)
    predicted_digit = np.argmax(prediction)  # Get the digit with the highest probability
    print(f"The image is likely to be {predicted_digit}")

# Test with your image
predict_digit("001.jpg")
print()
predict_digit("002.png")