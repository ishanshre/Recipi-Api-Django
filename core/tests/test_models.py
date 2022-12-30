"""
Tests for models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

User = get_user_model()


class ModelTests(TestCase):
    """Test Models"""
    def test_create_user_with_email_successfull(self):
        """Testing creating a user with an email is successfull"""
        email = "testing@gmail.com"
        password = "testpass@123"
        username = "test"
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1','test1@EXAMPLE.com','test1@example.com'],
            ['test2','Test2@Example.COM','Test2@example.com'],
            ['test3','TEST3@EXAMPLE.COM','TEST3@example.com'],
            ['test4','test4@example.COM','test4@example.com'],
        ]

        for username, email, expected in sample_emails:
            user = User.objects.create_user(username=username, email=email, password="hello123")
            self.assertEqual(user.email, expected)
    
    def test_new_user_without_username_raises_error(self):
        """Test creating new user without username will raises ValueError"""
        with self.assertRaises(ValueError):
            User.objects.create_user(username="",email="admin212@asd.com",password="hello@123")
            
    
    def test_recipi_create(self):
        """Test create new recipi"""
        user = User.objects.create_user(
            email="test@email.com",
            username="test",
            password="hello@123"
        )
        recipi = models.Recipi.objects.create(
            user=user,
            title="create new recipi",
            description="This is description",
            time_minutes=13,
            price=1000
        )
        self.assertEqual(str(recipi), recipi.title)