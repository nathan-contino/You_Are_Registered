from django import forms
from models import Courses

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    email = forms.EmailField(max_length=200,required=True)
    password = forms.CharField(max_length=200,required=True, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    password = forms.CharField(max_length=200,required=True, widget=forms.PasswordInput())

class RegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        allClasses = Courses.objects.all()
        for i in range(len(allClasses)):
            self.fields['%s %s %s-%s %s %s %s' % (allClasses[i].crsnum, allClasses[i].title, allClasses[i].start, allClasses[i].end, allClasses[i].building, allClasses[i].room, allClasses[i].prof)] = forms.BooleanField(required=False)
