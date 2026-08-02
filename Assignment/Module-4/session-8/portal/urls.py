from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
]
