from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это главная страница проекта Homework DJ01</h1>")
from django.shortcuts import render

# Create your views here.
def data(request):
    return HttpResponse("<h1>Это страница data проекта Homework DJ01</h1>")

def test(request):
    return HttpResponse("<h1>Это страница test проекта Homework DJ01</h1>")