from django.urls import path
from application_3.views import index ,catalog5, catalog6

urlpatterns = [
    path('index3/', index),
    path('catalog5/', catalog5),
    path('catalog6/', catalog6),
]