from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def sign_up(request):
    fm = UserCreationForm()
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    return render(request,'enroll/signup.html',{'form':fm})