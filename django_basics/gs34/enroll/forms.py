from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your Name')
    email = forms.EmailField()
    mobile = forms.IntegerField()
    key = forms.CharField(widget=forms.HiddenInput)