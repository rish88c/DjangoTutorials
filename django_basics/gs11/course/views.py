from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Home Page')


def learn_django(request):
    coursename={'cname':'django'}
    return render(request,'course/course1.html',context=coursename)


def learn_python(request):
    return render(request, 'course/course2.html')


def learn_var(request):
    a = "<h1>Hello variable</h1>"
    return HttpResponse(a)


def learn_math(request):
    a = 10+10
    return HttpResponse(a)


def learn_format(request):
    a = 'Geeky Shoes'
    return HttpResponse(f'Hello how are you {a}')
