from django.shortcuts import render, HttpResponse, redirect
from .models import Cources
from .models import Form

# Create your views here.


def home(request):
    data = Cources.objects.all()
    return render(request, 'home.html', {'data': data})


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        password = request.POST.get('password')

        form_entry = Form(
            name=name,
            email=email,
            message=message,
            password=password
        )
        form_entry.save()
        return HttpResponse("Form submitted successfully!")

    return render(request, 'form.html')


def delete_content_page(request):
    data = Form.objects.all()
    return render(request, 'delete_content.html', {'data': data})


def delete_content(request, id):
    form_entry = Form.objects.get(id=id)
    form_entry.delete()
    return redirect('delete')


def delete_course(request, course_id):
    course = Cources.objects.get(id=course_id)
    course.delete()
    return HttpResponse("Course deleted successfully!")
