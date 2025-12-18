from django.db import models

# Create your models here.


class Cources(models.model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
