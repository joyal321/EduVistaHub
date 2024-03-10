from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('about',views.about,name="about"),
    path('course',views.course,name="course"),
    path('contact',views.contact,name="contact"),
    path('python_full_stack',views.python,name="python"),
    path('python_AI',views.py_ai,name="python_ai"),
    path('Html_Course',views.html,name="html"),
    path('big_data',views.big_data_c,name="big_data"),
    
]