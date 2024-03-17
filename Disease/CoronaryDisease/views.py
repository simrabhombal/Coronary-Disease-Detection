# CoronaryDisease/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from .forms import UploadImageForm
from .ml_predict import preprocess_image, predict_ecg_image  # Import your image preprocessing function
from keras.models import load_model  # Import Keras model loading function
import numpy as np
import os

model_path = os.path.normpath("D://my project//newcnn_c.h5")

if os.path.exists(model_path):
    cnn_model = load_model(model_path)
else:
    raise FileNotFoundError(f"The model file '{model_path}' does not exist.")

label_encoder_classes = ['abnormal', 'myocardial_infarction', 'normal']

import logging

logger = logging.getLogger(__name__)
def result(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            ecg_image = request.FILES['ecg_image']
            if not ecg_image.content_type.startswith('image'):
                return HttpResponseServerError("Uploaded file is not an image.")
            
            try:
                # Preprocess the uploaded image
                processed_image = preprocess_image(ecg_image, target_size=(224, 224))
                processed_image = np.reshape(processed_image, (1, 224, 224, 3))
                
                # Make predictions using the CNN model
                predictions = cnn_model.predict(processed_image)
                predicted_class_index = np.argmax(predictions)
                predicted_class_label = label_encoder_classes[predicted_class_index]

                # Render the result page with the prediction result
                return render(request, 'result.html', {'predicted_class_label': predicted_class_label, 'form': form})

            except Exception as e:
                return HttpResponseServerError("Error processing the uploaded image")

    return HttpResponseRedirect(reverse('home'))

def home(request):
    form = UploadImageForm()
    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')
