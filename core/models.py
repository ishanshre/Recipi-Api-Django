from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Recipi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipies')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    link = models.URLField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title