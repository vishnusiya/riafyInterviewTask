import requests #Vishnupriya
from django.conf import settings#Vishnupriya
from django.shortcuts import render




def home(request):
    return render(request, 'home.html')
