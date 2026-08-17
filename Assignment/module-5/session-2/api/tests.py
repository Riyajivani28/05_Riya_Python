from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Restaurant

class RestaurantAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.restaurant = Restaurant.objects.create(
            name="Tasty Bites",
            cuisine="Italian",
            rating=4.5
        )

    def test_apiview_create(self):
        data = {"name": "Burger Hub", "cuisine": "American", "rating": 4.2}
        response = self.client.post("/api/restaurants/apiview/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Burger Hub")

    def test_apiview_list(self):
        response = self.client.get("/api/restaurants/apiview/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_apiview_update_put(self):
        data = {"name": "Tasty Bites Updated", "cuisine": "Italian", "rating": 4.8}
        response = self.client.put(f"/api/restaurants/apiview/{self.restaurant.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Tasty Bites Updated")

    def test_apiview_update_patch(self):
        data = {"rating": 4.9}
        response = self.client.patch(f"/api/restaurants/apiview/{self.restaurant.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["rating"], 4.9)

    def test_apiview_delete(self):
        response = self.client.delete(f"/api/restaurants/apiview/{self.restaurant.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Restaurant.objects.count(), 0)

    def test_apiview_not_found(self):
        response = self.client.get("/api/restaurants/apiview/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_generic_mixin_create(self):
        data = {"name": "Sushi Express", "cuisine": "Japanese", "rating": 4.7}
        response = self.client.post("/api/restaurants/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_generic_mixin_list(self):
        response = self.client.get("/api/restaurants/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_generic_mixin_update_put(self):
        data = {"name": "Tasty Bites", "cuisine": "Mexican", "rating": 4.0}
        response = self.client.put(f"/api/restaurants/{self.restaurant.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_generic_mixin_update_patch(self):
        data = {"rating": 5.0}
        response = self.client.patch(f"/api/restaurants/{self.restaurant.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_generic_mixin_delete(self):
        response = self.client.delete(f"/api/restaurants/{self.restaurant.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
