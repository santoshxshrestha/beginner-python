from django.shortcuts import render
# importing the Student model to send data to frond en d
from .models import Student

# Create your views here.


# View for the home page
def home(request):
    data = Student.objects.all()
    return render(request, "index.html", {"students": data})
