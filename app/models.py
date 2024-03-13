from django.db import models

# Create your models here.
class Registration(models.Model):
    uname    = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pswd = models.CharField(max_length=100)
    conpass    = models.CharField(max_length=100)