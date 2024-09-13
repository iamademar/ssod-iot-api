from django.db import models

class Reading(models.Model):
    room_name = models.CharField(max_length=255)
    sensor_name = models.CharField(max_length=255)
    reading = models.FloatField()
    datetime_recorded_by_sensor = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_name} - {self.sensor_name} - {self.date_recorded}"