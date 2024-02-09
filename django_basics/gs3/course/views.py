from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Home Page')

def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')
