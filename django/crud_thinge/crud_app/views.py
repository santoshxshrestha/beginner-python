from django.shortcuts import render
from .models import Cources

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

    return render(request, 'form.html')
