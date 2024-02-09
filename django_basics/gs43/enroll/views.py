from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.

# def thankyou(request):
#     return render(request,'enroll/success.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # name =fm.cleaned_data['name']
            # email = fm.cleaned_data['email']
            # password = fm.cleaned_data['password']
            print('Form Validated')
            print('Name:',fm.cleaned_data['name'])
            print('Email',fm.cleaned_data['email'])
            print('Password',fm.cleaned_data['password'])
            print('RPassword', fm.cleaned_data['rpassword'])
            # return HttpResponseRedirect('/en/success/')
            # return render(request, 'enroll/success.html',{'nm':name})
            
    else:
        fm = StudentRegistration()
    
    return render(request, 'enroll/userregistration.html',{'form':fm})