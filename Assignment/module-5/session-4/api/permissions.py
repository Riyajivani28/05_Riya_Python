from rest_framework.permissions import BasePermission

class IsPremiumUser(BasePermission):
    """
    Custom permission to only allow access to users with is_premium=True.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            getattr(request.user, 'is_premium', False)
        )
