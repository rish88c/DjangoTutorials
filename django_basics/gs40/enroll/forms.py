from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_name(self):
        valname = self.cleaned_data.get('name')
        if len(valname)<4:
            raise forms.ValidationError('Enter more than 4 character')
        else:
            return valname
