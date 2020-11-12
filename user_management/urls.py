from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import login



urlpatterns = [

    url(r'^login/$',login,name="user-login"), 
    url(r'^logout/$',login,name="user-login"), 

]

