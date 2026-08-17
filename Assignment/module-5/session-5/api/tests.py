from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class ExternalAPIEndpointsTests(APITestCase):

    # 1. Test /api/music-weather/<city>/
    def test_music_weather_contains_temperature_and_description(self):
        url = reverse('music-weather', kwargs={'city': 'London'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('temperature', response.data)
        self.assertIn('description', response.data)

    # 2. Test /api/food-location/?restaurant=Dominos
    def test_food_location_success(self):
        url = f"{reverse('food-location')}?restaurant=Dominos"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('latitude', response.data)
        self.assertIn('longitude', response.data)

    def test_food_location_missing_param(self):
        url = reverse('food-location')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    # 3. Test /api/country-info/<country_name>/
    def test_country_info_success(self):
        url = reverse('country-info', kwargs={'country_name': 'India'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('population', response.data)
        self.assertIn('capital', response.data)

    def test_country_info_invalid(self):
        url = reverse('country-info', kwargs={'country_name': 'InvalidCountryXYZ999'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)

    # 4. Test /api/github-repos/<username>/
    def test_github_repos_success(self):
        url = reverse('github-repos', kwargs={'username': 'octocat'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('repositories', response.data)
        self.assertIsInstance(response.data['repositories'], list)

    def test_github_repos_invalid_user(self):
        url = reverse('github-repos', kwargs={'username': 'nonexistentuser999999999999'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)

