from django.contrib import admin
from django.urls import path , include
from MyApp import views

urlpatterns = [
    path('a1/', views.Display),
    path('a2/', views.Display2),
    path('a3/', views.Intro1)
]