"""fypdia2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from getdata import views    # need this from the views.py
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
import accounts.views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    # shows JSON lists in the URL to be parsed by the app and displayed to the user
    url(r'^clients/', views.ClientList.as_view()),
    url(r'^lessons/', views.LessonList.as_view()),
    url(r'^locations/', views.LocationList.as_view()),
    url(r'^users/', views.UserList.as_view()),
    url(r'^expenses/', views.ExpenseList.as_view()),

]

