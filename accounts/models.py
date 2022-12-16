from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class GENDER_CHOICE(models.TextChoices):
    MALE = "M",'Male'
    FEMALE = "F",'Female'
    OTHERS = "O",'Others'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE.choices, null=True, blank=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="image/user/profile", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username.title()}'s Profile"



