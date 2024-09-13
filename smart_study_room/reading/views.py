from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Reading
from .serializers import ReadingSerializer
from occupancy.authentication import APIKeyAuthentication
from occupancy.permissions import HasValidAPIKey

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