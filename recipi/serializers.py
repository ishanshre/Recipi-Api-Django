"""
Serializers for recipi app
"""

from rest_framework import serializers

from core.models import Recipi


class RecipiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipi
        fields = ['id','title','description','time_minutes','price','link','created','updated']
        read_only_fields = ['id']