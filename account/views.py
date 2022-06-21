from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        password_ = request.POST['password']
        username_ = request.POST['username']
        user = auth.authenticate(request, username=username_, password=password_)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        User.objects.create_user(username=request.POST['username'], password=request.POST['password'], studentId=request.POST['studentId'])
        return redirect('profile')
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')
