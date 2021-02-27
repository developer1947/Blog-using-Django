from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Index(request):
    return render(request, 'MainApp/index.html')

def login(request):
    return render(request, 'MainApp/login.html')

def Register(request):
    return render(request, 'MainApp/Register.html')

def About(request):
    return render(request, 'MainApp/About.html')

def Gallery(request):
    return render(request, 'MainApp/Gallery.html')