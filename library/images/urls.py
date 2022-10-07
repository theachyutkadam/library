from django.contrib import admin
from django.urls import path, include
from images import views

urlpatterns = [
    path('', views.index, name='images'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout')
]
