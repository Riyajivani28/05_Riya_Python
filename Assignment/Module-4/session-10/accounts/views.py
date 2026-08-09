import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.conf import settings
from .forms import ForgotPasswordForm, OTPVerificationForm

def forgot_password_view(request):
    """
    Renders a form where users enter their email to request a password reset.
    Generates a random 6-digit OTP, stores it in session with a 5-minute expiration,
    and sends it to the user's email using send_mail with a colorful HTML design.
    """
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Generate random 6-digit OTP
            otp = f"{random.randint(100000, 999999):06d}"
            
            # Store in session
            request.session['otp'] = otp
            request.session['user_email'] = email
            
            # Set session expiry time of 5 minutes (300 seconds)
            request.session.set_expiry(300)
            
            # Render colorful HTML email template
            html_message = render_to_string('accounts/email_otp.html', {
                'otp': otp,
                'user_email': email
            })
            plain_message = strip_tags(html_message)
            
            subject = 'Password Reset OTP'
            from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com')
            
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=from_email,
                recipient_list=[email],
                html_message=html_message,
                fail_silently=False,
            )
            
            messages.success(request, f'A 6-digit OTP has been sent to {email}.')
            return redirect('verify_otp')
    else:
        form = ForgotPasswordForm()
        
    return render(request, 'accounts/forgot_password.html', {'form': form})


def verify_otp_view(request):
    """
    Builds a Django form where the user enters the OTP received via email,
    validates the OTP by comparing it with the value stored in session,
    and displays a success or error message accordingly.
    """
    verified = False
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            user_otp = form.cleaned_data['otp']
            session_otp = request.session.get('otp')
            
            if session_otp and str(user_otp).strip() == str(session_otp).strip():
                messages.success(request, 'OTP Verified Successfully!')
                verified = True
                # Remove OTP from session once successfully verified
                if 'otp' in request.session:
                    del request.session['otp']
            else:
                messages.error(request, 'Invalid or expired OTP. Please try again.')
    else:
        form = OTPVerificationForm()
        
    return render(request, 'accounts/verify_otp.html', {'form': form, 'verified': verified})
