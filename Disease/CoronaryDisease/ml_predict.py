# ml_predict.py

import os
import cv2
import numpy as np
from keras.models import load_model

model_path = "D:\\MY PROJECT\\newcnn_c.h5"
if os.path.exists("D:\\MY PROJECT\\newcnn_c.h5"):
    cnn_model = load_model("D:\\MY PROJECT\\newcnn_c.h5")
else:
    raise FileNotFoundError(f"The model file '{model_path}' does not exist.")

# Define the target size for image resizing
target_size = (224, 224)

import cv2
import numpy as np



def preprocess_image(image_file, target_size):
    # Convert the image file to a NumPy array
    image = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    
    # Decode the image array using OpenCV
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    # Resize the image to the target size
    image = cv2.resize(image, target_size)
    
    # Normalize pixel values to the range [0, 1]
    image = image / 255.0

    return image


def predict_ecg_image(image_file):
    # Read the image file
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Preprocess the image
    preprocessed_image = preprocess_image(image, target_size)

    # Make predictions using the CNN model
    predictions = cnn_model.predict(np.expand_dims(preprocessed_image, axis=0))

    # Decode the predictions (you may need to adapt this based on your label encoding)
    classes = ['normal', 'abnormal', 'myocardial_infarction']
    decoded_prediction = classes[np.argmax(predictions)]

    # Return the prediction result
    return decoded_prediction

