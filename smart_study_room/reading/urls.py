from django.urls import path
from .views import create_reading

urlpatterns = [
    path('create/', create_reading, name='create_reading'),
]