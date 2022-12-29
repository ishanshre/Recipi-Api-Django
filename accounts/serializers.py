"""
Serializers for User API Endpoints
"""

from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for new user creation"""
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ["username","email","password"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
