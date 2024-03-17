# CoronaryDisease/forms.py
from django import forms

class UploadImageForm(forms.Form):
    ecg_image = forms.ImageField(label='Choose an ECG Image', widget=forms.ClearableFileInput(attrs={'class': 'form-control-file mt-2'}))
