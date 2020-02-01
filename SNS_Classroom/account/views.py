from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.models import UserRole
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
            messages.error(request, f"Login Error")
            return render(request, 'login.html')
        else:
            login(request, user)
            messages.success(request, f"Logged in Successfully")
            return redirect("/")

# Anons can't visit this page
def view_signup(request):
    if request.method == "GET" and checkRole(request, "admin"):
        return render(request, 'signup.html')
    else:
        user = User.objects.create_user(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            username=request.POST['username'], 
            email=request.POST['email'], 
            password=request.POST['password']
        )
        if request.POST['role'] == 'admin':
            print("super")
            user.is_superuser = user.is_staff = 1
        userRole = UserRole(
            user=user,
            role=request.POST['role']
        )
        user.save()
        userRole.save()
        login(request, user)
        messages.success(request, f"Signed up Successfully")
        return redirect("/")

def view_logout(request):
    logout(request)
    messages.success(request, f"Logged out Successfully")
    return redirect("/")

def checkRole(request, role):
    if request.user.userrole.role == role:
        return True
    else:
        return False
    
