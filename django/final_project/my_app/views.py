from django.shortcuts import render, redirect
from django import forms
# importing the Student model to send data to frond en d
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age', 'address']

# Create your views here.


# View for the home page
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    data = Student.objects.all()
    return render(request, "index.html", {"students": data, "form": form})


def students(request):
    data = Student.objects.all()
    return render(request, "students.html", {"students": data})


def edit_data(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, "edit_student.html", {"student": student})


def update_data(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.email = request.POST.get("email")
        student.age = request.POST.get("age")
        student.address = request.POST.get("address")
        student.save()
    return redirect('home')


def delete_data(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('home')
