from rest_framework.permissions import BasePermission

class HasValidAPIKey(BasePermission):
    def has_permission(self, request, view):
        return request.auth is not None