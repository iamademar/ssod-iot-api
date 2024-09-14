from django.urls import path
from .views import create_reading, get_latest_readings

urlpatterns = [
    path('create/', create_reading, name='create_reading'),
    path('latest/', get_latest_readings, name='get_latest_readings'),
]