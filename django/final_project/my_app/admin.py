from django.contrib import admin
from .models import Student

# Register your models here.

# registering the Students model to make it accessible
# via the Django admin page
admin.site.register(Student)
