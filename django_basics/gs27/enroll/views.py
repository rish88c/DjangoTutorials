from django.shortcuts import render
from ...gs28.enroll.forms import StudentRegistration
# Create your views here.

def showdate(request):
    fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm})