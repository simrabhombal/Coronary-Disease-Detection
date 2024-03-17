# CoronaryDisease/urls.py

from django.urls import path
from . import views 
from .views import base, home, about, login, contact, result

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('result/', result, name='result'),
   # path('predict/', predict_coronary_disease, name='predict_coronary_disease'),
]

