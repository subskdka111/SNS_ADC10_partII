from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def view_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            HttpResponse("error")
        else:
            login(request, user)
            return redirect("/")

def view_signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        user = User.objects.create_user(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            username=request.POST['username'], 
            email=request.POST['email'], 
            password=request.POST['password'])
        if request.POST['role'] == 'admin':
            user.is_superuser = user.is_staff = 1
        elif request.POST['role'] == 'staff':
            user.is_staff = 1
        else:
            user.is_staff = 0
        user.save()
        login(request, user)
        return redirect("/")

def view_logout(request):
    logout(request)
    return redirect("/")
