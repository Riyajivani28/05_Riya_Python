from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class APIEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_send_email_missing_param(self):
        response = self.client.post(reverse('send-email'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email field is required", response.data.get('message', ''))

    def test_send_email_with_param(self):
        response = self.client.post(reverse('send-email'), {'email': 'user@example.com'}, format='json')
        # Expect either 200 or 400 depending on Mailgun API key validity, but must return structured JSON
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_400_BAD_REQUEST, status.HTTP_500_INTERNAL_SERVER_ERROR])
        self.assertIn('status', response.data)

    def test_send_sms_missing_params(self):
        response = self.client.post(reverse('send-sms'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('status', response.data)

    def test_send_sms_with_params(self):
        response = self.client.post(reverse('send-sms'), {
            'phone_number': '+15005550006',
            'message': 'Test SMS message'
        }, format='json')
        self.assertIn('status', response.data)

    def test_pay_missing_amount(self):
        response = self.client.post(reverse('pay'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('status'), 'error')

    def test_pay_valid_amount(self):
        response = self.client.post(reverse('pay'), {
            'amount': 50.0,
            'currency': 'usd'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('payment_status', response.data)
        self.assertIn('transaction_id', response.data)
        self.assertEqual(response.data.get('amount'), 50.0)

    def test_google_login_missing_token(self):
        response = self.client.post(reverse('google-login'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_google_login_test_token(self):
        response = self.client.post(reverse('google-login'), {
            'id_token': 'test_google_token_123',
            'email': 'john.doe@gmail.com'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data.get('user', {}).get('email'), 'john.doe@gmail.com')
