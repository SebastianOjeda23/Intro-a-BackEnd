from django.contrib import admin
from django.urls import path , include
from Myapp2 import views

urlpatterns = [
    path('a1/', views.bienvenio)
]