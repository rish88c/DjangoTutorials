from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("django/", views.learn_django,name='courseone'),
]
