from django.urls import path
from .views import save_room_occupancy, check_room_occupancy, get_latest_occupancy_logs, get_latest_room_temperature, get_reading_logs

urlpatterns = [
    path('sensor', save_room_occupancy),  # URL endpoint to save room occupancy data
    path('check_occupancy/<str:room_name>/', check_room_occupancy),  # URL endpoint to check room occupancy
    # path('sensor/logs', get_latest_occupancy_logs),  # URL endpoint to get latest occupancy logs
    path('temperature/<str:room_name>/', get_latest_room_temperature),  # URL endpoint to get temperature
    path('reading/logs', get_reading_logs),  # URL endpoint to get reading logs
]
