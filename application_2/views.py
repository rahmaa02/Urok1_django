from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse ('Приложение 2 Ф.П.1')

def catalog3(request):
    return HttpResponse ('Приложение 2 Ф.П.2')

def catalog4(request):
    return HttpResponse ('Приложение 2 Ф.П.3')