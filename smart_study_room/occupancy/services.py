from django.utils import timezone
from datetime import timedelta
from .models import RoomOccupancy

def is_room_occupied(room_name):
    # Calculate the timestamp for 3 minutes ago
    three_minutes_ago = timezone.now() - timedelta(minutes=3)
    
    # Query the database for the most recent room occupancy record
    latest_record = RoomOccupancy.objects.filter(
        room_name=room_name,
        timestamp__gte=three_minutes_ago
    ).order_by('-timestamp').first()
    
    # If no records found, the room is considered unoccupied
    if not latest_record:
        return False
    
    # Return True if the latest record shows presence, False otherwise
    return latest_record.presence_detected