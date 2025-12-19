from django.db import models

# Create your models here.


class Cources(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()


class Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    password = models.CharField(max_length=20)


