from django.urls import path
from .views import save_room_occupancy

urlpatterns = [
    path('sensor', save_room_occupancy),  # URL endpoint to save room occupancy data
]
