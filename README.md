# Coronary-Disease-Detection
# Coronary Disease Detection Using ECG Images

## Introduction

Coronary artery disease (CAD) remains one of the leading causes of morbidity and mortality worldwide. CAD occurs when the coronary arteries, which supply blood to the heart muscle, become narrowed or blocked due to the buildup of plaque. This condition can lead to severe complications such as heart attacks, angina, and sudden cardiac death.

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
