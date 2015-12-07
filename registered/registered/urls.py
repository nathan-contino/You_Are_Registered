"""registered URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
     url(r'^auth2/create_account.html','auth2.views.create_user', name='create_user'),
     url(r'^auth2/login.html','auth2.views.login_user', name='login'),
     url(r'^auth2/loggedin.html', 'auth2.views.loginpage'),
     url(r'^auth2/loggedout.html', 'auth2.views.logout_user'),
     url(r'^auth2/createsuccess.html', 'auth2.views.createsuccess'),
     url(r'^auth2/invalid.html', 'auth2.views.invalidusername'),
     url(r'^auth2/nologin.html', 'auth2.views.logout_user'),
     url(r'^auth2/schedule.html', 'auth2.views.schedule'),
     url(r'^auth2/addclass.html', 'auth2.views.addclass', name='crn'),
     url(r'^','auth2.views.login_user'),
]
