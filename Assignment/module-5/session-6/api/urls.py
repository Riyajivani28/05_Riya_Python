from django.urls import path
from .views import SendEmailView, SendSMSView, PayView, GoogleLoginView

urlpatterns = [
    path('send-email/', SendEmailView.as_view(), name='send-email'),
    path('send-sms/', SendSMSView.as_view(), name='send-sms'),
    path('pay/', PayView.as_view(), name='pay'),
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),
    path('auth/google/', GoogleLoginView.as_view(), name='auth-google'),
]
