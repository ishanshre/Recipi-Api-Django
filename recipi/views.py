from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from recipi.serializers import (
    RecipiSerializer
)

from core.models import Recipi
# Create your views here.

class RecipiViewSet(ModelViewSet):
    serializer_class = RecipiSerializer
    queryset = Recipi.objects.all()
    
