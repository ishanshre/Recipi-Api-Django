"""
Views for User API endpoints
"""
from rest_framework import generics

from accounts.serializers import UserCreateSerializer


class UserCreateApiView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserCreateSerializer