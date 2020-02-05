from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.models import UserRole
from module.models import Module
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from account.checkRole import *

def view_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            messages.error(request, f"Login Error")
            return render(request, 'login.html')
        else:
            login(request, user)
            messages.success(request, f"Logged in Successfully")
            return redirect("/")

def view_signup(request):
    if checkRole(request, "admin"):
        if request.method == "GET":
            return render(request, 'signup.html')
        
        if request.method == "POST":
            if User.objects.filter(username=request.POST['username']):
                messages.error(request, "Username already defined")
                return redirect("/signup")
            
            user = User.objects.create_user(
                first_name=request.POST['first_name'], 
                last_name=request.POST['last_name'], 
                username=request.POST['username'], 
                email=request.POST['email'], 
                password=request.POST['password']
            )
            if request.POST['role'] == 'admin':
                user.is_superuser = user.is_staff = 1
                
            userRole = UserRole(
                user=user,
                role=request.POST['role']
            )
            user.save()
            userRole.save()
            login(request, user)
            messages.success(request, f"Signed up Successfully")
    else:
        messages.success(request, "Only admins can create user")
    return redirect("/")

def view_profile(request, id):
    if request.method == "GET" and request.user.is_authenticated:
        requestedProfile = User.objects.get(id=id)
        if requestedProfile.userrole.role == "student":
            module = request.user.student.all()
        elif requestedProfile.userrole.role == "teacher" and Module.objects.get(moduleTeacher=requestedProfile):
            module = Module.objects.get(moduleTeacher=requestedProfile)
        else:
            module = ''
        print(module)
        context_variable = {
            'profile' : requestedProfile,
            'modules' : module
        }
        return render(request, "profile.html", context_variable)
    return redirect("/")

def view_logout(request):
    logout(request)
    messages.success(request, f"Logged out Successfully")
    return redirect("/")
