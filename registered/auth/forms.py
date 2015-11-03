from django import forms

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    email = forms.EmailField(max_length=200,required=True)
    password = forms.CharField(max_length=200,required=True)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    password = forms.CharField(max_length=200,required=True)
