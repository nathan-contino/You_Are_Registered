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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
     url(r'^auth/create_account.html','auth.views.create_user', name='create_user'),
     url(r'^auth/login.html','auth.views.login_user', name='login'),
     url(r'^auth/loggedin.html', 'auth.views.loginpage'),
     url(r'^auth/loggedout.html', 'auth.views.logout_user'),
     url(r'^auth/createsuccess.html', 'auth.views.createsuccess'),
     url(r'^auth/invalid.html', 'auth.views.invalidusername'),
     url(r'^auth/nologin.html', 'auth.views.logout_user'),
     url(r'^','auth.views.login_user'),
]
