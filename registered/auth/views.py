from django.shortcuts import render
from .forms import CreateUserForm, LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

csc210C = ["CSC 210", "MWF 9:00-9:50", "DEWEY 1101", "GUO", 0]
csc171C = ["CSC 171", "MW 12:30-1:45", "MEL 101", "FERGUSON", 0]
csc172C = ["CSC 172", "TR 9:40-10:55", "B&L 203", "PAWLICKI", 0]
csc173C = ["CSC 173", "MW 2:00-3:15", "HOYT AUD", "SEIFERES", 0]


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
        if request.method == 'GET':
            registeredCourses = request.user.classes.split(" ")
            csc210Bool = False
            csc171Bool = False
            csc172Bool = False
            csc173Bool = False
            if len(registeredCourses) > 3 :
                if registeredCourses[0] == "1":
                    csc210Bool = True
                if registeredCourses[1] == "1":
                    csc171Bool = True
                if registeredCourses[2] == "1":
                    csc172Bool = True
                if registeredCourses[3] == "1":
                    csc173Bool = True
            form = RegistrationForm(initial={"csc210": csc210Bool, "csc171": csc171Bool,"csc172": csc172Bool, "csc173": csc173Bool})
            addMessage = False

        else:
            form = RegistrationForm(request.POST) # Bind data from request.POST into a PostForm

            if form.is_valid():
                courseString = ""
                takingcourse = form.cleaned_data['csc210']
                if takingcourse:
                    courseString += "1"
                else:
                    courseString += "0"
                takingcourse2 = form.cleaned_data['csc171']
                if takingcourse2:
                    courseString += " 1"
                else:
                    courseString += " 0"
                takingcourse3 = form.cleaned_data['csc172']
                if takingcourse3:
                    courseString += " 1"
                else:
                    courseString += " 0"
                takingcourse4 = form.cleaned_data['csc173']
                if takingcourse4:
                    courseString += " 1"
                else:
                    courseString += " 0"
                request.user.classes = courseString
                request.user.save()
                return HttpResponseRedirect('/auth/schedule.html')

        return render(request, 'loggedin.html',
            {'full_name': request.user.username,
            'form': form,
            'addMessage': addMessage})
    return render_to_response('nologin.html')


def logout_user(request):
    logout(request)
    return render(request, 'loggedout.html')

def redirect_logout(request):
    return HttpResponseRedirect('/auth/loggedout.html')

def schedule(request):
    count = courseCount()
    if len(count) > 3:
        csc210C[4]=count[0]
        csc171C[4]=count[1]
        csc172C[4]=count[2]
        csc173C[4]=count[3]
    registeredCourses = request.user.classes.split(" ")
    courses =[]
    if len(registeredCourses) > 3 :
        if registeredCourses[0] == "1":
            courses.append(csc210C)
        if registeredCourses[1] == "1":
            courses.append(csc171C)
        if registeredCourses[2] == "1":
            courses.append(csc172C)
        if registeredCourses[3] == "1":
            courses.append(csc173C)
    print courses
    return render(request, 'schedule.html',
        {'size':len(courses),
        'courses': courses})



def courseCount() :
    csc210 = 0
    csc171 = 0
    csc172 = 0
    csc173 = 0
    users = User.objects.all()
    for user in users:
        registeredCourses = user.classes.split(" ")
        if len(registeredCourses) > 3 :
            if registeredCourses[0] == "1":
                csc210 += 1
            if registeredCourses[1] == "1":
                csc171 += 1
            if registeredCourses[2] == "1":
                csc172 += 1
            if registeredCourses[3] == "1":
                csc173 += 1
    arryNums = [csc210, csc171, csc172, csc173]
    return arryNums
