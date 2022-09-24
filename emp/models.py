from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    department=models.CharField(max_length=45)
    emp_isActive=models.BooleanField(default=True)

    # costomise admin pannel
    def __str__(self) -> str:
        return self.emp_id
    

