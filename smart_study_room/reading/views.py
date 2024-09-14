from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Reading
from .serializers import ReadingSerializer
from occupancy.authentication import APIKeyAuthentication
from occupancy.permissions import HasValidAPIKey

import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@authentication_classes([APIKeyAuthentication])
@permission_classes([HasValidAPIKey])
def create_reading(request):
    if request.method == 'POST':
        serializer = ReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([APIKeyAuthentication])
@permission_classes([HasValidAPIKey])
def get_latest_readings(request):
    latest_readings = Reading.objects.order_by('-created_at')[:10]
    logs_data = [
        {
            'id': log.id,
            'room_name': log.room_name,
            'sensor_name': log.sensor_name,
            'reading': log.reading,
            'datetime_recorded_by_sensor': log.datetime_recorded_by_sensor.isoformat()
        }
        for log in latest_readings
    ]
    return JsonResponse({'logs': logs_data})