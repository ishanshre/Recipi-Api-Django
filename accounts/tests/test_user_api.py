"""
Test for user API endpoints
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


User = get_user_model()
CREATE_URL_URL = reverse("accounts:create")

def create_user(**params):
    """Create and return new user"""
    return User.objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public feature of the user api endpoint"""
    def setUp(self):
        self.client = APIClient()
    
    def test_user_create_success(self):
        """Test create user success"""
        payload = {
            "username":"user",
            "email":"user@example.com",
            "password":"test@123"
        }
        res = self.client.post(CREATE_URL_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username=payload['username'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn(payload['password'], res.data)

    def test_user_with_username_exists_error(self):
        """Test error returned if user with username already exists"""
        payload = {
            "username":"user",
            "email":"user@example.com",
            "password":"test@123",
        }
        create_user(**payload)
        res = self.client.post(CREATE_URL_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test error returned if password too short"""
        payload = {
            "username":"user",
            "email":"user@gmail.com",
            "password":"hell"
        }
        res = self.client.post(CREATE_URL_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = User.objects.filter(username=payload['username']).exists()
        self.assertFalse(user_exists)