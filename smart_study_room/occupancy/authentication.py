from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_X_API_KEY')
        if not api_key:
            return None

        if api_key != settings.API_KEY:
            raise AuthenticationFailed('Invalid API key')

        return (None, True)  # Return True for auth to indicate successful authentication