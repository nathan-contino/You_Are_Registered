from django import forms

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    email = forms.EmailField(max_length=200,required=True)
    password = forms.CharField(max_length=200,required=True)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    password = forms.CharField(max_length=200,required=True)

class RegistrationForm(forms.Form):
    csc210 = forms.BooleanField(required=False)
    csc171 = forms.BooleanField(required=False)
    csc172 = forms.BooleanField(required=False)
    csc173 = forms.BooleanField(required=False)
