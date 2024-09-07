from django.utils import timezone
from datetime import timedelta
from .models import RoomOccupancy

def is_room_occupied(room_name):
    # Calculate the timestamp for 3 minutes ago
    three_minutes_ago = timezone.now() - timedelta(minutes=3)
    
    # Query the database for room occupancy records:
    # 1. Filter by room name and timestamps within the last 3 minutes
    # 2. Order by sensor name (ascending) and timestamp (descending)
    # 3. Select the most recent record for each sensor
    records = (RoomOccupancy.objects.filter(room_name=room_name, timestamp__gte=three_minutes_ago)
               .order_by('sensor_name', '-timestamp')
               .distinct('sensor_name'))
    
    # If no records found, the room is considered unoccupied
    if not records.exists():
        return False
    
    presence_detected_by_all_sensors = True
    # Check each sensor's most recent record
    for record in records:
        if not record.presence_detected:
            presence_detected_by_all_sensors = False
            break
    
    return presence_detected_by_all_sensors