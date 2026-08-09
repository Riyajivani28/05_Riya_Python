from django.shortcuts import redirect
from django.urls import reverse

class BlockExpiredOTPAccessMiddleware:
    """
    Middleware that checks if the OTP session key is missing or expired.
    If so, redirects users trying to access the OTP verification page back to the forgot password form.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            verify_otp_url = reverse('verify_otp')
        except Exception:
            verify_otp_url = '/verify-otp/'

        if request.path == verify_otp_url:
            otp = request.session.get('otp')
            if 'otp' not in request.session or not otp:
                return redirect('forgot_password')

        response = self.get_response(request)
        return response
