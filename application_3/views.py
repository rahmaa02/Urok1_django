from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse ('Приложение 3 Ф.П.1')

def catalog5(request):
    return HttpResponse ('Приложение 3 Ф.П.2')

def catalog6(request):
    return HttpResponse ('Приложение 3 Ф.П.3')