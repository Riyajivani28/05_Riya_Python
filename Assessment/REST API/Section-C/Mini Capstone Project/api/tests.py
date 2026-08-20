from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Category, MenuItem, Order

class CategoryAPITests(APITestCase):
    def test_category_creation_and_list(self):
        url = '/api/categories/'
        data = {'name': 'Beverages', 'description': 'Refreshing drinks'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Beverages')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        self.assertEqual(len(results), 1)

class MenuItemAPITests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Pizza', description='Italian Pizza')

    def test_menu_item_creation(self):
        url = '/api/menu-items/'
        data = {
            'name': 'Margherita Pizza',
            'price': '12.99',
            'category': self.category.id,
            'is_available': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 1)

    def test_invalid_menu_item_price(self):
        url = '/api/menu-items/'
        data = {
            'name': 'Invalid Price Item',
            'price': '0.00',
            'category': self.category.id,
            'is_available': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)

        data['price'] = '-5.00'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class OrderAPITests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.token1 = Token.objects.create(user=self.user1)

        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.token2 = Token.objects.create(user=self.user2)

        self.category = Category.objects.create(name='Burger', description='Juicy Burgers')
        self.item1 = MenuItem.objects.create(name='Cheese Burger', price='8.99', category=self.category)
        self.item2 = MenuItem.objects.create(name='Veggie Burger', price='7.99', category=self.category)

    def test_unauthorized_order_request(self):
        url = '/api/orders/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(url, {'item': self.item1.id, 'quantity': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_order_creation_with_authentication(self):
        url = '/api/orders/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        data = {
            'item': self.item1.id,
            'quantity': 2,
            'status': 'pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.get()
        self.assertEqual(order.user, self.user1)
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.status, 'pending')

    def test_quantity_validation(self):
        url = '/api/orders/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        data = {
            'item': self.item1.id,
            'quantity': 0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('quantity', response.data)

    def test_order_listing_and_user_isolation(self):
        order1 = Order.objects.create(user=self.user1, item=self.item1, quantity=1, status='pending')
        order2 = Order.objects.create(user=self.user2, item=self.item2, quantity=3, status='confirmed')

        url = '/api/orders/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['id'], order1.id)

    def test_user_cannot_access_another_users_order(self):
        order2 = Order.objects.create(user=self.user2, item=self.item2, quantity=3, status='confirmed')
        url = f'/api/orders/{order2.id}/'

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_order_pagination(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        for i in range(7):
            Order.objects.create(user=self.user1, item=self.item1, quantity=1, status='pending')

        url = '/api/orders/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 7)
        self.assertEqual(len(response.data['results']), 5)
        self.assertIsNotNone(response.data['next'])

    def test_order_status_filtering(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        Order.objects.create(user=self.user1, item=self.item1, quantity=1, status='pending')
        Order.objects.create(user=self.user1, item=self.item2, quantity=2, status='confirmed')
        Order.objects.create(user=self.user1, item=self.item1, quantity=1, status='delivered')

        url = '/api/orders/?status=confirmed'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['status'], 'confirmed')
