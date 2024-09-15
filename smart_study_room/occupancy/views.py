from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import RoomOccupancy
from reading.models import Reading
from .serializers import RoomOccupancySerializer
from .authentication import APIKeyAuthentication
from .permissions import HasValidAPIKey
from .services import is_room_occupied

@api_view(['POST'])
@authentication_classes([APIKeyAuthentication])
@permission_classes([HasValidAPIKey])
def save_room_occupancy(request):
    if request.method == 'POST':
        serializer = RoomOccupancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([APIKeyAuthentication])
@permission_classes([HasValidAPIKey])
def check_room_occupancy(request, room_name):    
    occupied = is_room_occupied(room_name)
    return Response({'occupied': occupied}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([APIKeyAuthentication])
@permission_classes([HasValidAPIKey])
def get_latest_occupancy_logs(request):
    latest_logs = RoomOccupancy.objects.order_by('-timestamp')[:10]
    logs_data = [
        {
            'id': log.id,
            'room_name': log.room_name,
            'sensor_name': log.sensor_name,
            'presence_detected': log.presence_detected,
            'timestamp': log.timestamp.isoformat()
        }
        for log in latest_logs
    ]
    return JsonResponse({'logs': logs_data})

@api_view(['GET'])
@authentication_classes([APIKeyAuthentication])
@permission_classes([HasValidAPIKey])
def get_latest_room_temperature(request, room_name):
    try:
        latest_occupancy = RoomOccupancy.objects.filter(room_name=room_name).latest('timestamp')
        return JsonResponse({
            'room_name': room_name,
            'temperature': latest_occupancy.temperature,
            'timestamp': latest_occupancy.timestamp
        })
    except RoomOccupancy.DoesNotExist:
        return JsonResponse({
            'error': f'No temperature data found for room: {room_name}'
        }, status=404)
    
@api_view(['GET'])
@authentication_classes([APIKeyAuthentication])
@permission_classes([HasValidAPIKey])
def get_reading_logs(request):
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