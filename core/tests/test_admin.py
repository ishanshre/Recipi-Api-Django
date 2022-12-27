"""
Test Django admin customization
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class AdminSiteTests(TestCase):
    """Test for Django admin."""
    def setUp(self):
        """
        The code set up in this method is going to be run before every single test that we add to this class
        Create user and client
        """
        # this client is a Django Test Client that would allow us to make hasty type requests and then self to admin
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            email="admin123@email.com",
            username="admin123",
            password="test@123",
        )
        # force login method to force authenticat with super use we created
        self.client.force_login(self.admin_user)
        self.user = User.objects.create_user(
            email="user123@email.com",
            username="user123",
            password="test@123",
        )
    
    def test_users_list_works(self):
        """Test that the user are listed on the page."""
        url = reverse("admin:accounts_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.is_staff)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email_verified)
    
    def test_edit_user_page_works(self):
        """Test the edit user page works"""
        url = reverse("admin:accounts_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page_works(self):
        """Test the create user page works"""
        url = reverse("admin:accounts_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)




