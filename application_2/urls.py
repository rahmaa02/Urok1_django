from django.urls import path
from application_2.views import index ,catalog3, catalog4

urlpatterns = [
    path('index2/', index),
    path('upgrade2/', catalog3),
    path('upgrade3/', catalog4),
]