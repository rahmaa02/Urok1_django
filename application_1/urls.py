from django.urls import path
from application_1.views import index,catalog, catalog2

urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('catalog2/', catalog2),
]