from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

def validate_phone_number(value):
    if value and (not value.isdigit() or len(value) != 10):
        raise ValidationError('Phone number must be exactly 10 digits.')

class InfluencerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='influencerprofile')
    display_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, validators=[validate_phone_number])

    def __str__(self):
        return self.display_name or self.user.username

@receiver(post_save, sender=User)
def create_or_update_influencer_profile(sender, instance, created, **kwargs):
    if created:
        InfluencerProfile.objects.create(user=instance)
    elif not hasattr(instance, 'influencerprofile'):
        InfluencerProfile.objects.create(user=instance)
