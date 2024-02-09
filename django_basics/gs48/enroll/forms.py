from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Name','password':'Enter Password','email':'Enter Email'}
        help_text = {'name':'Enter your full name'}
        error_messages = {'name':{'required':'Naam likhna jaruri hai'},
                          'password':{'required':'Password Likhna Jaruri hai'}}
        widgets = {'password':forms.PasswordInput,
                   'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Yaha naam likhe'})}