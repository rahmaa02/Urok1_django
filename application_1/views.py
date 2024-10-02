from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Приложение 1 Ф.П.1')

def catalog(request):
    return HttpResponse('Приложение 1 Ф.П.2')

def catalog2(request):
    return HttpResponse('Приложение 1 Ф.П.3')