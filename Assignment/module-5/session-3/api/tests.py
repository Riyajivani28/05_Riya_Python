from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Restaurant

class RestaurantAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Seed test database with restaurants having different cuisines and names
        self.r1 = Restaurant.objects.create(name='Bella Italia', cuisine='Italian', location='Uptown')
        self.r2 = Restaurant.objects.create(name='Curry House', cuisine='Indian', location='City Center')
        self.r3 = Restaurant.objects.create(name='Dragon Wok', cuisine='Chinese', location='Eastside')
        self.r4 = Restaurant.objects.create(name='Pasta Palace', cuisine='Italian', location='Downtown')
        self.r5 = Restaurant.objects.create(name='Sushi Spot', cuisine='Japanese', location='Harbor View')
        self.r6 = Restaurant.objects.create(name='Taco Town', cuisine='Mexican', location='West End')

    def test_restaurant_model_fields(self):
        """Test Restaurant model creation with exact fields (name, cuisine, location)."""
        restaurant = Restaurant.objects.get(id=self.r1.id)
        self.assertEqual(restaurant.name, 'Bella Italia')
        self.assertEqual(restaurant.cuisine, 'Italian')
        self.assertEqual(restaurant.location, 'Uptown')

    def test_api_restaurants_endpoint(self):
        """Test GET /api/restaurants/ endpoint exists and returns 200."""
        response = self.client.get('/api/restaurants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_limit_offset_pagination(self):
        """Test /api/restaurants/?limit=2&offset=2 works correctly."""
        response = self.client.get('/api/restaurants/?limit=2&offset=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn('count', data)
        self.assertEqual(data['count'], 6)
        self.assertEqual(len(data['results']), 2)

    def test_ordering_by_name(self):
        """Test /api/restaurants/?ordering=name returns restaurants ordered alphabetically by name."""
        response = self.client.get('/api/restaurants/?ordering=name')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        names = [r['name'] for r in results]
        self.assertEqual(names, sorted(names))

    def test_ordering_by_cuisine_descending(self):
        """Test /api/restaurants/?ordering=-cuisine returns restaurants sorted descending by cuisine."""
        response = self.client.get('/api/restaurants/?ordering=-cuisine')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        cuisines = [r['cuisine'] for r in results]
        self.assertEqual(cuisines, sorted(cuisines, reverse=True))

    def test_cuisine_filter(self):
        """Test /api/restaurants/?cuisine=Italian filters restaurants by cuisine."""
        response = self.client.get('/api/restaurants/?cuisine=Italian')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        self.assertEqual(len(results), 2)
        for r in results:
            self.assertEqual(r['cuisine'], 'Italian')
