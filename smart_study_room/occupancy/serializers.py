from rest_framework import serializers
from .models import RoomOccupancy

class RoomOccupancySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomOccupancy
        fields = '__all__'