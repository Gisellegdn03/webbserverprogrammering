from django.urls import path
from django.urls import include
from . import views
from django.contrib import admin




urlpatterns = [
    path('', views.hello, name="hello"),
    path('about/', views.about, name="cool"),
    path('contact/', views.contact, name="contact"),
]












