import random
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from twilio.rest import Client
from .forms import RegistrationForm, OTPRequestForm, OTPVerifyForm
from .models import Profile, OTPVerification
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            mobile_number = form.cleaned_data.get('mobile_number')
            Profile.objects.create(user=user, mobile_number=mobile_number) # not verified yet
            
            # Send Mailgun Welcome Email
            try:
                mailgun_url = f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages"
                auth = ("api", settings.MAILGUN_API_KEY)
                data = {
                    "from": f"AuthVault <{settings.MAILGUN_FROM_EMAIL}>",
                    "to": [user.email],
                    "subject": "Welcome to AuthVault!",
                    "text": f"Hello {user.username},\n\nWelcome to AuthVault!\n\nYour account has been successfully created."
                }
                requests.post(mailgun_url, auth=auth, data=data)
            except Exception as e:
                pass # Fail silently for email on registration
                
            # Log the user in so they can access the OTP verify view
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            # Generate and Send OTP
            otp_code = str(random.randint(100000, 999999))
            OTPVerification.objects.create(
                user=user,
                mobile_number=mobile_number,
                otp_code=otp_code
            )
            
            msg = f"Your AuthVault verification code is: {otp_code}. It expires in 5 minutes."
            send_twilio_sms(mobile_number, msg)
            
            request.session['otp_mobile_number'] = mobile_number
            messages.success(request, "Account created successfully! Please verify your mobile number.")
            return redirect('otp_verify')
    else:
        form = RegistrationForm()
        
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

def send_twilio_sms(to_number, message_body):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_number
        )
        return True
    except Exception as e:
        print(f"Twilio Error: {e}")
        return False

@login_required
def otp_request_view(request):
    if request.method == 'POST':
        form = OTPRequestForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            
            # Generate 6 digit OTP
            # Note: For production, consider hashing this before saving
            # Security limitation: Storing plain OTPs in DB is insecure against DB breaches.
            otp_code = str(random.randint(100000, 999999))
            
            # Deactivate previous unverified OTPs for this user
            OTPVerification.objects.filter(user=request.user, is_verified=False).update(is_verified=True)
            
            otp_obj = OTPVerification.objects.create(
                user=request.user,
                mobile_number=mobile_number,
                otp_code=otp_code
            )
            
            # Send SMS
            msg = f"Your verification code is: {otp_code}. It expires in 5 minutes."
            if send_twilio_sms(mobile_number, msg):
                messages.success(request, "OTP sent successfully to your mobile number.")
                # Save mobile number in session for verification step
                request.session['otp_mobile_number'] = mobile_number
                return redirect('otp_verify')
            else:
                messages.error(request, "Failed to send OTP. Please check your Twilio configuration.")
    else:
        form = OTPRequestForm()
    
    return render(request, 'otp_request.html', {'form': form})

@login_required
def otp_verify_view(request):
    mobile_number = request.session.get('otp_mobile_number')
    if not mobile_number:
        messages.error(request, "No pending OTP request found.")
        return redirect('otp_request')
        
    if request.method == 'POST':
        form = OTPVerifyForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp_code']
            
            try:
                otp_obj = OTPVerification.objects.get(
                    user=request.user, 
                    mobile_number=mobile_number,
                    is_verified=False
                )
                
                # Check expiration
                if timezone.now() > otp_obj.expires_at:
                    messages.error(request, "OTP has expired. Please request a new OTP.")
                    return redirect('otp_request')
                    
                # Check attempts
                if otp_obj.attempts >= 3:
                    messages.error(request, "Too many incorrect attempts. Please request a new OTP.")
                    otp_obj.is_verified = True # mark invalid
                    otp_obj.save()
                    return redirect('otp_request')
                    
                # Verify code
                if otp_obj.otp_code == entered_otp:
                    otp_obj.is_verified = True
                    otp_obj.save()
                    
                    # Update user profile with verified mobile number
                    profile, created = Profile.objects.get_or_create(user=request.user)
                    profile.mobile_number = mobile_number
                    profile.save()
                    
                    messages.success(request, "OTP verified successfully.")
                    
                    # Clear session
                    if 'otp_mobile_number' in request.session:
                        del request.session['otp_mobile_number']
                        
                    return redirect('dashboard')
                else:
                    otp_obj.attempts += 1
                    otp_obj.save()
                    messages.error(request, "Invalid OTP.")
            except OTPVerification.DoesNotExist:
                messages.error(request, "No valid OTP request found or already verified.")
    else:
        form = OTPVerifyForm()
        
    return render(request, 'otp_verify.html', {'form': form, 'mobile_number': mobile_number})
