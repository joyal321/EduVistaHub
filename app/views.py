from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

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


