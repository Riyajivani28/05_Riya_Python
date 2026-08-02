from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from .models import InfluencerProfile
from .forms import InfluencerProfileForm
import os

class InfluencerProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile, _ = InfluencerProfile.objects.get_or_create(user=self.user)
        self.client = Client()
        self.client.login(username='testuser', password='password123')

    def test_media_settings(self):
        self.assertEqual(settings.MEDIA_URL, '/media/')
        self.assertTrue(str(settings.MEDIA_ROOT).endswith('user_uploads'))

    def test_phone_number_validation_valid(self):
        form = InfluencerProfileForm(data={
            'display_name': 'Test Display',
            'bio': 'Test Bio',
            'phone_number': '1234567890'
        }, instance=self.profile)
        self.assertTrue(form.is_valid())

    def test_phone_number_validation_invalid_length(self):
        form = InfluencerProfileForm(data={
            'display_name': 'Test Display',
            'bio': 'Test Bio',
            'phone_number': '123456789'  # 9 digits
        }, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)
        self.assertEqual(form.errors['phone_number'][0], 'Phone number must be exactly 10 digits.')

    def test_phone_number_validation_non_digits(self):
        form = InfluencerProfileForm(data={
            'display_name': 'Test Display',
            'bio': 'Test Bio',
            'phone_number': '12345abcde'  # non-digits
        }, instance=self.profile)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)

    def test_profile_upload_and_display(self):
        # Create a small 1x1 gif image for testing upload
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff'
            b'\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
        )
        image_file = SimpleUploadedFile('test_avatar.gif', small_gif, content_type='image/gif')

        response = self.client.post('/profile/edit/', {
            'display_name': 'Super Star',
            'bio': 'Fashion & Lifestyle Creator',
            'phone_number': '9876543210',
            'profile_pic': image_file,
        })
        self.assertRedirects(response, '/')

        self.profile.refresh_from_db()
        self.assertEqual(self.profile.display_name, 'Super Star')
        self.assertEqual(self.profile.phone_number, '9876543210')
        self.assertTrue(self.profile.profile_pic.name.startswith('profile_pics/'))

        # Test profile view rendering
        view_response = self.client.get('/')
        self.assertContains(view_response, 'Super Star')
        self.assertContains(view_response, '9876543210')
        self.assertContains(view_response, self.profile.profile_pic.url)

    def test_default_avatar_fallback(self):
        # Profile without pic should render default avatar
        self.profile.profile_pic = None
        self.profile.save()

        view_response = self.client.get('/')
        self.assertContains(view_response, 'default_avatar.svg')
