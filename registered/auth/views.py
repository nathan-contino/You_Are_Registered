from django.shortcuts import render
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

def create_user(request):
    if request.method == 'GET':
        form = CreateUserForm()
    else:
        form = CreateUserForm(request.POST) # Bind data from request.POST into a PostForm

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                return HttpResponseRedirect('/auth/createsuccess.html')
            except:
                return HttpResponseRedirect('/auth/invalid.html')


    return render(request, 'createuser.html', {
        'form': form,
    })
def createsuccess(request):
    return render(request, 'createsuccess.html')

def invalidusername(request):
    return render(request, 'invalid.html')

def login_user(request):
    if len(request.user.username) > 0:
        return HttpResponseRedirect('/auth/loggedin.html')
    else:
        if request.method == 'GET':
            form = LoginForm()
        else:
            form = LoginForm(request.POST) # Bind data from request.POST into a PostForm

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect('/auth/loggedin.html')

                        # Redirect to a success page.

        return render(request, 'login.html', {
            'form': form,
            })


def loginpage(request):
    if request.user is not None:
        return render_to_response('loggedin.html',
            {'full_name': request.user.username})
    return render_to_response('nologin.html')


def logout_user(request):
    logout(request)
    return render(request, 'loggedout.html')

def redirect_logout(request):
    return HttpResponseRedirect('/auth/loggedout.html')
