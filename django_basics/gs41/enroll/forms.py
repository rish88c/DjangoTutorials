from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valname = cleaned_data.get('name')  # Use get() to avoid KeyError
        valemail = cleaned_data.get('email')  # Use get() to avoid KeyError

        if valname and len(valname) < 4:
            raise forms.ValidationError(
                "Name should be more than or equal to 4 characters")

        if valemail and len(valemail) < 10:
            raise forms.ValidationError(
                "Email should be more than or equal to 10 characters")
