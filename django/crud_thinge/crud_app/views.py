from django.shortcuts import render
from .models import Cources

# Create your views here.


def home(request):
    data = Cources.objects.all()
    return render(request, 'home.html', {'data': data})
