from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Collect the data to show on the frontpage
def home(request):
    context = {
        'title':'Home',
    }
    return render(request,'home.html',context)

# collect data to show on the admin page
def admin(request):
    pass
    context = {
        'title':'Admin',
    }
    return render(request, 'admin.html', context)

# collect data to show on the about page
def about(request):
    pass
    context = {
        'title':'About',
    }
    return render(request, 'about.html', context)

# collect data to show on the student page
def student(request):
    pass
    context = {
        'title':'Student',
    }
    return render(request, 'student.html', context)

# collect data to show on the teacher page
def teacher(request):
    pass
    context = {
        'title':'Teacher',
    }
    return render(request, 'teacher.html', context)

# the login page
def user_login(request):
    context = {
        'title':'Login',
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, "Welcome {}".format(username))
                return redirect('index')
    else:
        form = LoginForm()
    
    context['form'] = form
    return render(request, 'login.html', context )

# to create a new user
def signup(request):
    context = {
        'title':'Signup',
    }
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "user {} has been created\nPlease login".format(form.cleaned_data['username']))
            return redirect('login')
    else:
        form = SignupForm()
    
    context['form'] = form

    return render(request, 'signup.html', context)

# logout page
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('index')