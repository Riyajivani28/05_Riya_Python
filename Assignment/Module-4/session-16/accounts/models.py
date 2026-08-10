from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class UserProfile(models.fields.related.OneToOneField):
    # Actually, we can just use a standard model for Profile
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class OTPVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otp_verifications', null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_verified = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            # OTP expires in 5 minutes
            self.expires_at = timezone.now() + datetime.timedelta(minutes=5)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"OTP for {self.mobile_number}"
