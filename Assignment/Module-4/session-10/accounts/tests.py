from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail

class ForgotPasswordTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.forgot_url = reverse('forgot_password')
        self.verify_url = reverse('verify_otp')

    def test_forgot_password_get(self):
        response = self.client.get(self.forgot_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/forgot_password.html')

    def test_forgot_password_post_generates_otp_and_sends_email(self):
        test_email = 'user@example.com'
        response = self.client.post(self.forgot_url, {'email': test_email})
        
        # Check redirect to verify OTP
        self.assertRedirects(response, self.verify_url)
        
        # Check session key 'otp' exists and is 6 digits
        session = self.client.session
        self.assertIn('otp', session)
        otp = session['otp']
        self.assertTrue(otp.isdigit())
        self.assertEqual(len(otp), 6)
        
        # Check email sent via send_mail backend
        self.assertEqual(len(mail.outbox), 1)
        sent_mail = mail.outbox[0]
        self.assertIn(test_email, sent_mail.to)
        self.assertIn(otp, sent_mail.body)
        self.assertEqual(sent_mail.subject, 'Password Reset OTP')

    def test_middleware_blocks_access_when_otp_missing(self):
        # Trying to access verify_otp directly without OTP in session
        response = self.client.get(self.verify_url)
        # Should redirect to forgot_password
        self.assertRedirects(response, self.forgot_url)

    def test_middleware_allows_access_when_otp_in_session(self):
        # Set session OTP first
        session = self.client.session
        session['otp'] = '123456'
        session.save()
        
        # Access verify_otp page
        response = self.client.get(self.verify_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/verify_otp.html')

    def test_otp_verification_success(self):
        session = self.client.session
        session['otp'] = '654321'
        session.save()
        
        response = self.client.post(self.verify_url, {'otp': '654321'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'OTP Verified Successfully!')

    def test_otp_verification_failure_incorrect_otp(self):
        session = self.client.session
        session['otp'] = '654321'
        session.save()
        
        response = self.client.post(self.verify_url, {'otp': '111111'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid or expired OTP')
