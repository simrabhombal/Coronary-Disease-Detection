
# Coronary Disease Detection by ECG Images using Machine Learning

## Introduction

Coronary disease remains one of the leading causes of morbidity and mortality worldwide. CAD occurs when the coronary arteries, which supply blood to the heart muscle, become narrowed or blocked due to the buildup of plaque. This condition can lead to severe complications such as heart attacks, angina, and sudden cardiac death.

Early detection and accurate diagnosis of coronary disease are crucial for effective intervention and treatment. Traditional diagnostic methods, such as stress tests and coronary angiography, can be invasive, costly, and time-consuming. As a result, there is a growing need for non-invasive, efficient, and accurate diagnostic tools.

### Project Motivation

This project addresses the need for an automated system that can analyze ECG (electrocardiogram) images to detect coronary artery disease. ECG is a widely used diagnostic tool that records the electrical activity of the heart and is relatively inexpensive and non-invasive. By leveraging machine learning techniques, particularly deep learning with Convolutional Neural Networks (CNNs), we aim to enhance the diagnostic accuracy and speed of ECG image analysis.

Our project integrates machine learning models to classify ECG images into three categories:
- **Normal:** Indicates a healthy heart with no evident signs of coronary disease.
- **Abnormal:** Suggests the presence of irregularities in heart activity that may require further investigation.
- **Myocardial Infarction:** Identifies signs indicative of a heart attack, a critical condition requiring immediate medical attention.

### Why This Project is Necessary

1. **Enhanced Diagnostic Accuracy:** Automated analysis using machine learning models can provide more accurate and consistent results compared to manual interpretation by clinicians, potentially reducing diagnostic errors.

2. **Early Detection:** Rapid and precise identification of coronary disease can lead to earlier intervention and treatment, which is crucial for improving patient outcomes and reducing the risk of severe complications.

3. **Accessibility:** By developing a user-friendly web application, we aim to make advanced diagnostic tools more accessible, allowing healthcare professionals to analyze ECG images efficiently, regardless of their location.

4. **Cost-Efficiency:** Reducing the need for expensive and invasive diagnostic procedures by using an automated system can lower healthcare costs and make diagnostics more affordable.

## Features

- **ECG Image Classification:** Classify ECG images into normal, abnormal, or myocardial infarction categories using machine learning models.
- **Django Web Interface:** A web application designed with Tailwind CSS for a modern and responsive user experience.
- **High Accuracy:** The CNN model, which demonstrated the highest classification accuracy among the tested models, is used for precise diagnostics.

## Prerequisites

To run this project, you need to have the following software and libraries installed:

### Software

- **Python 3.9 or above**: Make sure you have Python 3.9 or higher installed. You can download it from [python.org](https://www.python.org/).

- **pip**: Python's package installer. It usually comes with Python installations. If not, you can install it by following the instructions at [pip documentation](https://pip.pypa.io/en/stable/installation/).

- **Django**: A high-level Python web framework that you’ll use to build the web application.

- ### Python Libraries

Install the required Python libraries using the `requirements.txt` file, which includes the following:

1. **TensorFlow**: A deep learning framework used to build and train the Convolutional Neural Network (CNN).
   ```bash
   pip install tensorflow
2. **scikit-learn**: A library for traditional machine learning algorithms, including Naive Bayes, SVM, and Random Forest.
   ```bash
   pip install scikit-learn
3. **Django**: The web framework used to create the user interface.
   ```bash
   pip install django
4. **NumPy**: A library for numerical operations, often used for handling arrays and matrices in data preprocessing.
   ```bash
   pip install numpy
5. **Matplotlib**: A plotting library used for visualizing data and results.
   ```bash
   pip install matplotlib
6. **OpenCV**: A library for computer vision tasks that might be useful for additional image processing.
   ```bash
   pip install opencv-python
7. **pandas**: A data manipulation and analysis library, used for handling structured data.
   ```bash
   pip install pandas

### Installation Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/simrabhombal/Coronary-Disease-Detection.git
   cd Coronary-Disease-Detection
2. **Set Up Dataset Directory**:
   Ensure that your dataset directory is correctly set up and accessible. Place your ECG images in the appropriate directory as required by your project. You may need to configure file paths in your project settings or code.
3. **Navigate to the Project Directory**:
   Ensure you are in the root directory of your Django project (where manage.py is located).
   ```bash
   cd Disease
4. **Run the Development Server**:
   Start the Django development server to access the web application:
   ```bash
   python manage.py runserver
5. **Access the Application**:
Open your web browser and navigate to 'http://127.0.0.1:8000/'.

## Demo Video
   https://streamable.com/bko6oh
