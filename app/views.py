from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['pass']
        log = authenticate(request, uname=username,
                            pswd=password)
        
        if log is not None:
            login(request, log)
            messages.error(request, 'Logged in Fail')
            return redirect('login')
        
        else:
            messages.success(request, 'Logged in successfully')
            return redirect('index')
    #     checkpswd = check_password()
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        data = Registration(uname = request.POST['username'], email = request.POST['mail'], pswd = make_password(request.POST['pass']), conpass = make_password(request.POST['cpass']))
        data.save()
        return render(request, 'index.html')    
    return render(request, 'register.html')


def about(request):
    return render(request,'about.html')

def course(request):
    return render(request,'course.html')

def contact(request):
    return render(request,'contact.html')

def python(request):
    return render(request,'python_full_stack.html')

def py_ai(request):
    return render(request,'python_ai.html')

def html(request):
    return render(request,'html_c.html')

def big_data_c(request):
    return render(request,'big_data_c.html')


