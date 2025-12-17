from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello, welcome to the home page!")


def another_home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def portfolio(request):
    return render(request, "portfolio.html")
