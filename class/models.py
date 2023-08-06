from django.db import models
from accounts.models import User

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=20)


    def __str__(self):
        return self.name
    
    


