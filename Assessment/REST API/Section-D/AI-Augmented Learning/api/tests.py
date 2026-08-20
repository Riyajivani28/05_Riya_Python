from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order

class PlaceOrderAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/orders/place/'

    def test_place_order_success(self):
        data = {
            "customer_name": "Riya",
            "item": "Pizza",
            "quantity": 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['customer_name'], "Riya")
        self.assertEqual(response.data['item'], "Pizza")
        self.assertEqual(response.data['quantity'], 2)
        self.assertIn('id', response.data)
        self.assertEqual(Order.objects.count(), 1)

    def test_place_order_invalid_quantity_zero(self):
        data = {
            "customer_name": "Riya",
            "item": "Pizza",
            "quantity": 0
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Quantity must be a positive integer."})
        self.assertEqual(Order.objects.count(), 0)

    def test_place_order_invalid_quantity_negative(self):
        data = {
            "customer_name": "Riya",
            "item": "Pizza",
            "quantity": -3
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Quantity must be a positive integer."})

    def test_place_order_invalid_quantity_type(self):
        data = {
            "customer_name": "Riya",
            "item": "Pizza",
            "quantity": "two"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Quantity must be a positive integer."})
