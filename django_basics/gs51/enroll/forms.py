from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50,required=False)
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Name','password':'Enter Password','email':'Enter Email'}
        help_text = {'name':'Enter your full name'}
        widgets = {'password':forms.PasswordInput}