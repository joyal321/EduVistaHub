from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',admin_login,name="ad_login"),
    path('dashboard',dashboard,name="ad_dashboard"),

]