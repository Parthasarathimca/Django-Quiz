from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        
        username=request.GET.get('username')
        password=request.GET.get('password')
 
        user = User.objects.get(username=username)
        
        if user:
            if user.check_password(password):
                django_login(request, user)            

    if request.method == 'GET':
        data={}
        return render(request,'login.html',data)
def logout(request):
    auth.logout(request)
    data={}
    return render(request, 'login.html',data)
    