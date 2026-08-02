from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

DEFAULT_EMAIL = getattr(settings, 'EMAIL_HOST_USER', 'riyajivani85@gmail.com')

def email_index(request):
    """Dashboard page showing form cards for all email tools."""
    return render(request, 'email_app/index.html')


# Task 1: Simple Test Email View with HTML Design
def send_simple_test_email(request):
    """
    Renders form on GET. Sends test email with HTML styling using send_mail on POST.
    """
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email', DEFAULT_EMAIL)
        subject = request.POST.get('subject', 'Django Test Email')
        message_text = request.POST.get('message', 'Hello! This is a simple test email sent using Django send_mail.')
        from_email = settings.DEFAULT_FROM_EMAIL

        # Render HTML template for Gmail styling
        html_content = render_to_string('test_email_template.html', {
            'subject': subject,
            'message': message_text
        })

        try:
            send_mail(
                subject=subject,
                message=message_text,
                from_email=from_email,
                recipient_list=[recipient_email],
                html_message=html_content,
                fail_silently=False
            )
            messages.success(request, f"Simple test email sent successfully to {recipient_email}!")
        except Exception as e:
            messages.error(request, f"Failed to send email: {e}")

        return render(request, 'email_app/test_email.html', {'default_email': recipient_email})

    return render(request, 'email_app/test_email.html', {'default_email': DEFAULT_EMAIL})


# Task 2: Password Reset Email View with Paytm/Flipkart HTML Design
def send_password_reset_email(request, user_email=None):
    """
    Renders form on GET. Sends Paytm style password reset HTML email using send_mail on POST.
    """
    if request.method == 'POST':
        target_email = request.POST.get('user_email', user_email or DEFAULT_EMAIL)
        app_name = request.POST.get('app_name', 'Paytm')
        subject = f"Reset your password - {app_name} Account"
        reset_link = 'http://127.0.0.1:8000/reset-password/token_xyz123/'
        
        plain_message = (
            f"Hi,\n\n"
            f"We received a request to reset your {app_name} account password.\n"
            f"Click the link below to set a new password:\n"
            f"{reset_link}\n\n"
            f"Regards,\n{app_name} Support"
        )

        html_content = render_to_string('password_reset_template.html', {
            'app_name': app_name,
            'user_email': target_email,
            'reset_link': reset_link
        })
        
        from_email = settings.DEFAULT_FROM_EMAIL

        try:
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=from_email,
                recipient_list=[target_email],
                html_message=html_content,
                fail_silently=False
            )
            messages.success(request, f"Password reset email sent to {target_email} successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send password reset email: {e}")

        return render(request, 'email_app/password_reset.html', {'default_email': target_email})

    return render(request, 'email_app/password_reset.html', {'default_email': user_email or DEFAULT_EMAIL})


# Task 3: Swiggy Order Confirmation Email View
def send_order_confirmation_email(request, user_email=None):
    """
    Renders form on GET. Sends Swiggy order confirmation HTML email using EmailMultiAlternatives on POST.
    """
    if request.method == 'POST':
        target_email = request.POST.get('user_email', user_email or DEFAULT_EMAIL)
        user_name = request.POST.get('user_name', 'Riya')
        order_id = request.POST.get('order_id', 'SWG987654')
        restaurant_name = request.POST.get('restaurant_name', 'Biryani Blues')
        delivery_address = request.POST.get('delivery_address', '101 Horizon Towers, SG Highway, Ahmedabad')
        total_amount = request.POST.get('total_amount', 650)

        subject = 'Swiggy Order Confirmation'
        from_email = settings.DEFAULT_FROM_EMAIL
        to = [target_email]

        context = {
            'user_name': user_name,
            'order_id': order_id,
            'restaurant_name': restaurant_name,
            'delivery_address': delivery_address,
            'items': [
                {'name': 'Chicken Dum Biryani', 'quantity': 1, 'price': 350},
                {'name': 'Paneer Tikka', 'quantity': 1, 'price': 220},
                {'name': 'Gulab Jamun (2 Pcs)', 'quantity': 1, 'price': 80},
            ],
            'total_amount': total_amount,
        }

        text_content = f"Hi {user_name}, your order #{order_id} from {restaurant_name} is confirmed! Total Amount: ₹{total_amount}."
        html_content = render_to_string('order_confirmation.html', context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")

        try:
            msg.send(fail_silently=False)
            messages.success(request, f"Swiggy order confirmation email sent to {target_email} successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send order confirmation email: {e}")

        return render(request, 'email_app/order_confirmation_form.html', {'default_email': target_email})

    return render(request, 'email_app/order_confirmation_form.html', {'default_email': user_email or DEFAULT_EMAIL})


# Task 4: IPL Fantasy Welcome Email View
def send_ipl_welcome_email(request, user_email=None):
    """
    Renders form on GET. Sends IPL Fantasy welcome HTML email using EmailMultiAlternatives on POST.
    """
    if request.method == 'POST':
        target_email = request.POST.get('user_email', user_email or DEFAULT_EMAIL)
        user_name = request.POST.get('user_name', 'Riya')
        subject = request.POST.get('subject', '🏏 Game On! Welcome to IPL Fantasy League 2026 - Build Your Dream XI Now! 🏆')

        from_email = settings.DEFAULT_FROM_EMAIL
        to = [target_email]

        context = {
            'user_name': user_name,
        }

        text_content = f"Welcome to IPL Fantasy League 2026, {user_name}! Build your dream XI and win exciting prizes."
        html_content = render_to_string('ipl_welcome.html', context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")

        try:
            msg.send(fail_silently=False)
            messages.success(request, f"IPL Fantasy League welcome email sent to {target_email} successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send IPL Fantasy welcome email: {e}")

        return render(request, 'email_app/ipl_welcome_form.html', {'default_email': target_email})

    return render(request, 'email_app/ipl_welcome_form.html', {'default_email': user_email or DEFAULT_EMAIL})
