import base64
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationAndPermissionTests(APITestCase):

    def setUp(self):
        # Create standard user (non-premium)
        self.standard_user = User.objects.create_user(
            username='standard_user',
            password='Password123!',
            is_premium=False
        )
        # Create premium user
        self.premium_user = User.objects.create_user(
            username='premium_user',
            password='Password123!',
            is_premium=True
        )
        # Generate Auth Token for standard user
        self.token = Token.objects.create(user=self.standard_user)

    # -------------------------------------------------------------
    # 1. Test /api/playlists/ (BasicAuthentication & IsAuthenticated)
    # -------------------------------------------------------------
    def test_playlists_unauthenticated_access_denied(self):
        url = reverse('playlist-list')
        response = self.client.get(url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_playlists_basic_auth_success(self):
        url = reverse('playlist-list')
        credentials = base64.b64encode(b'standard_user:Password123!').decode('utf-8')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Basic {credentials}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('playlists', response.data)

    # -------------------------------------------------------------
    # 2. Test /api/orders/ (TokenAuthentication & IsAuthenticated)
    # -------------------------------------------------------------
    def test_orders_without_token_denied(self):
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_orders_with_valid_token_success(self):
        url = reverse('order-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('orders', response.data)

    # -------------------------------------------------------------
    # 3. Test /api/cart/ (SessionAuthentication & IsAuthenticated)
    # -------------------------------------------------------------
    def test_cart_unauthenticated_user_403(self):
        url = reverse('cart-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cart_logged_in_user_success(self):
        url = reverse('cart-view')
        self.client.force_login(user=self.standard_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('cart', response.data)

    # -------------------------------------------------------------
    # 4. Test /api/tickets/ (Custom Permission: IsPremiumUser)
    # -------------------------------------------------------------
    def test_tickets_non_premium_user_access_denied(self):
        url = reverse('ticket-list')
        self.client.force_login(user=self.standard_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_tickets_premium_user_access_granted(self):
        url = reverse('ticket-list')
        self.client.force_login(user=self.premium_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tickets', response.data)
