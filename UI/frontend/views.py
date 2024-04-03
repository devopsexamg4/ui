from django.shortcuts import render
from django.http import HttpResponse

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