from django.contrib import admin
from django.urls import path
from.views import Index, login, Register, About, Gallery

urlpatterns = [
    path('',Index,name='Index'),
    path('login/',login,name='login'),
    path('Register/',Register,name='Register'),
    path('About/',About,name='About'),
    path('Gallery/',Gallery,name='Gallery'),


]
