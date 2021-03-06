# search filter multiple queries help: http://stackoverflow.com/questions/5445174/or-operator-in-django-model-queries
from django.shortcuts import render
from .forms import CreateUserForm, LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from models import Courses

csc210C = ["CSC 210", "MWF 9:00-9:50", "DEWEY 1101", "GUO", 0]
csc171C = ["CSC 171", "MW 12:30-1:45", "MEL 101", "FERGUSON", 0]
csc172C = ["CSC 172", "TR 9:40-10:55", "B&L 203", "PAWLICKI", 0]
csc173C = ["CSC 173", "MW 2:00-3:15", "HOYT AUD", "SEIFERAS", 0]
allClasses = [csc210C, csc171C, csc172C, csc173C]

def searchClasses(request):
    registeredCourses = request.user.classes.split(" ")
    regCourses = []
    for crn2 in registeredCourses:
        course2 = Courses.objects.filter(crn=crn2)
        if len(course2) > 0:
            course = course2[0]
            regCourses.append(course)
    searchTopic = request.GET.get('q')
    print searchTopic
    if searchTopic is not None:
        courses = Courses.objects.filter(Q(title__icontains=searchTopic) |
                               Q(crsnum__icontains=searchTopic) |
                               Q(prof__icontains=searchTopic))
    else:
        courses = Courses.objects.all()
    return render(request, 'loggedin.html',
    {'full_name': request.user.username,
    'form': "none",
    'addMessage': "none",
    'courses': courses,
    'regCourses':regCourses})

def addclass(request):
    delete = 0
    crn = request.GET.get("crn")
    registeredCourses = request.user.classes.split(" ")
    print registeredCourses
    crns = request.user.classes
    if crns == "":
        crns = crn
    else:
        if crn in registeredCourses:
            registeredCourses.remove(crn)
            newCourse = ""
            delete = 1
            for i in range(len(registeredCourses)):
                if i == 0:
                    newCourse = registeredCourses[0]
                else:
                    newCourse = newCourse + " " + registeredCourses[i]

            crns = newCourse
        else:
            crns = crns + " " + crn
    request.user.classes = crns
    request.user.save()
    course2 = Courses.objects.filter(crn=crn)
    if len(course2) > 0:
        course = course2[0]
        if delete > 0:
            course.current = int(course.current) - 1
        else:
            course.current = int(course.current) + 1
        course.save()
    return HttpResponse("Done!")


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
                return HttpResponseRedirect('/auth2/createsuccess.html')
            except:
                return HttpResponseRedirect('/auth2/invalid.html')


    return render(request, 'createuser.html', {
        'form': form,
    })
def createsuccess(request):
    return render(request, 'createsuccess.html')

def invalidusername(request):
    return render(request, 'invalid.html')

def login_user(request):
    if len(request.user.username) > 0:
        return HttpResponseRedirect('/auth2/loggedin.html')
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
                        return HttpResponseRedirect('/auth2/loggedin.html')

                        # Redirect to a success page.

        return render(request, 'login.html', {
            'form': form,
            })


def loginpage(request):
    if len(request.user.username) > 0:
        if request.method == 'GET':
            allClasses = Courses.objects.all()
            registeredCourses = request.user.classes.split(" ")
            form = RegistrationForm()
            regCourses = []
            for crn2 in registeredCourses:
                course2 = Courses.objects.filter(crn=crn2)
                if len(course2) > 0:
                    course = course2[0]
                    regCourses.append(course)
                    form.fields['%s %s %s-%s %s %s %s' % (course.crsnum, course.title, course.start, course.end, course.building, course.room, course.prof)].initial = True
            addMessage = False

        else:
            form = RegistrationForm(request.POST) # Bind data from request.POST into a PostForm

            if form.is_valid():
                allClasses = Courses.objects.all()
                crns = ""
                for i in range(len(allClasses)):
                    takingcourse=form.cleaned_data['%s %s %s-%s %s %s %s' % (allClasses[i].crsnum, allClasses[i].title, allClasses[i].start, allClasses[i].end, allClasses[i].building, allClasses[i].room, allClasses[i].prof)]
                    if takingcourse:
                        if crns == "":
                            crns = "%s" % allClasses[i].crn
                        else:
                            crns = crns+" %s" % allClasses[i].crn
            request.user.classes = crns
            request.user.save()
            return HttpResponseRedirect('/auth2/schedule.html')

        return render(request, 'loggedin.html',
            {'full_name': request.user.username,
            'form': form,
            'addMessage': addMessage,
            'courses': regCourses,
            'regCourses': regCourses})
    return render_to_response('nologin.html')


def logout_user(request):
    if len(request.user.username) > 0:
        logout(request)
        return render(request, 'loggedout.html')
    else:
       return render_to_response('nologin.html')

def redirect_logout(request):
    return HttpResponseRedirect('/auth2/loggedout.html')

def schedule(request):


    if len(request.user.username) > 0:
        registeredCourses = request.user.classes.split(" ")
        courses = []
        for crn2 in registeredCourses:
            print crn2
            course2 = Courses.objects.filter(crn=crn2)
            if len(course2) > 0:
                course = course2[0]
                t = course.title
                d = course.day + " " + course.start + "-" + course.end
                b = course.building + " " + course.room
                p = course.prof
                c = course.current
                cList = [t,d,b,p,c]
                courses.append(cList)

    # if len(request.user.username) > 0:
    #     count = courseCount()
    #     if len(count) > 3:
    #         csc210C[4]=count[0]
    #         csc171C[4]=count[1]
    #         csc172C[4]=count[2]
    #         csc173C[4]=count[3]
    #     registeredCourses = request.user.classes.split(" ")
    #     courses =[]
    #     if len(registeredCourses) > 3 :
    #         if registeredCourses[0] == "1":
    #             courses.append(csc210C)
    #         if registeredCourses[1] == "1":
    #             courses.append(csc171C)
    #         if registeredCourses[2] == "1":
    #             courses.append(csc172C)
    #         if registeredCourses[3] == "1":
    #             courses.append(csc173C)
    #     print courses
        return render(request, 'schedule.html',
            {'size':len(courses),
            'courses': courses})
    else:
       return render_to_response('nologin.html')




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
