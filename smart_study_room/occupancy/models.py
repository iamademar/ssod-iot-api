from django.db import models

class RoomOccupancy(models.Model):
    room_name = models.CharField(max_length=255)  # Name of the room
    presence_detected = models.BooleanField()  # Whether presence was detected
    temperature = models.DecimalField(max_digits=5, decimal_places=2)  # Temperature reading
    timestamp = models.DateTimeField(auto_now_add=True)  # Time when the reading was recorded

    def __str__(self):
        return f"{self.room_name} - {self.timestamp}"
