from django.db import models

# Create your models here.


# here we are creating a class named Meroclass to store the detials of the student
class Meroclass(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)

    # this will return the name of the class when we print the object in the admin panel
    def __str__(self):
        return self.name
