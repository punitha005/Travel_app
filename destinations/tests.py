from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Destination

class DestinationAPITestCase(APITestCase):
    """
    Integration tests for the Destination API endpoints.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.destination = Destination.objects.create(
            name="Test Destination",
            country="Test Country",
            description="Test Description",
            best_time_to_visit="Test Time",
            category="Beach",
            image_url="https://example.com/image.jpg"
        )

    def test_get_destinations(self):
        """
        Test retrieving the list of destinations.
        """
        response = self.client.get('/destinations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_destination_detail(self):
        """
        Test retrieving a specific destination.
        """
        response = self.client.get(f'/destinations/{self.destination.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Destination")

    def test_create_destination_authenticated(self):
        """
        Test creating a destination when authenticated.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "New Destination",
            "country": "New Country",
            "description": "New Description",
            "best_time_to_visit": "New Time",
            "category": "City",
            "image_url": "https://example.com/new_image.jpg"
        }
        response = self.client.post('/destinations/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_destination_unauthenticated(self):
        """
        Test creating a destination when unauthenticated.
        """
        data = {
            "name": "New Destination",
            "country": "New Country",
            "description": "New Description",
            "best_time_to_visit": "New Time",
            "category": "City",
            "image_url": "https://example.com/new_image.jpg"
        }
        response = self.client.post('/destinations/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_destination(self):
        """
        Test updating a destination.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "Updated Destination",
            "country": "Updated Country",
            "description": "Updated Description",
            "best_time_to_visit": "Updated Time",
            "category": "Mountain",
            "image_url": "https://example.com/updated_image.jpg"
        }
        response = self.client.put(f'/destinations/{self.destination.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Destination")

    def test_delete_destination(self):
        """
        Test deleting a destination.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/destinations/{self.destination.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Destination.objects.filter(id=self.destination.id).exists())
