from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.


def sign_up(request):
    fm = SignUpForm()
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!!')
            fm.save()
            fm = SignUpForm()

    return render(request, 'enroll/signup.html', {'form': fm})
