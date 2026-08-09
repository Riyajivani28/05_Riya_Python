from functools import wraps
from django.core.exceptions import PermissionDenied

def group_required(*group_names):
    """
    Decorator for views that checks whether a user has a specific group membership,
    raising PermissionDenied (403) if they do not. Superusers bypass this check.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                from django.contrib.auth.views import redirect_to_login
                return redirect_to_login(request.get_full_path())
            
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
                
            user_groups = request.user.groups.values_list('name', flat=True)
            if any(group in user_groups for group in group_names):
                return view_func(request, *args, **kwargs)
                
            raise PermissionDenied
        return _wrapped_view
    return decorator

def seller_required(view_func):
    return group_required('Seller')(view_func)

def buyer_required(view_func):
    return group_required('Buyer')(view_func)
