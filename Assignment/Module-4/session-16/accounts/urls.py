from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('otp/request/', views.otp_request_view, name='otp_request'),
    path('otp/verify/', views.otp_verify_view, name='otp_verify'),
]
