from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100,default='')
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=50,default='')
    branch = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=10,default='')

class AllAppointments(models.Model):
    name = models.CharField(max_length=100,default='')
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=50,default='')
    branch = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=10,default='')


    