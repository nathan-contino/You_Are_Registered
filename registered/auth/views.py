from django.shortcuts import render
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def create_user(request):
    if request.method == 'GET':
        form = CreateUserForm()
    else:
        form = CreateUserForm(request.POST) # Bind data from request.POST into a PostForm

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            return HttpResponse("Account Created Successfully!")

    return render(request, 'createuser.html', {
        'form': form,
    })

def login_user(request):
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
                    print "YESSSS"
                    login(request,user)
                    # Redirect to a success page.




    return render(request, 'login.html', {
        'form': form,
    })
