from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField(max_length=200)
    student_college=models.CharField(max_length=200)
    student_city=models.CharField(max_length=30)
    student_age=models.IntegerField()
    is_active=models.BooleanField(default=False)
    
