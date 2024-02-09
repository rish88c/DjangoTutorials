from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5, max_length=10, strip=False, error_messages={
                           'required': 'enter your name'})
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    roll_No = forms.IntegerField(min_value=5)
    
    agree = forms.BooleanField(label_suffix='',label='I Agree')

