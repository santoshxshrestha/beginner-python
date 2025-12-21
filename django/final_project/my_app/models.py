from django.db import models

# Create your models here.


# here student id is primary key by default so it will be
# generate automatically and
# will be unique for each student
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    address = models.TextField()
