from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"
    username= None
    email = models.EmailField("Email", blank=False, null=False, unique=True)
    imageUrl = models.TextField(default= "test", null=False, blank=False) 
    restaurant_admin = models.BooleanField(default=True)
    
    objects = CustomUserManager()
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class TokenValidation(models.Model):

    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=10, null=False, blank=False)
    timeCreated = models.DateTimeField(auto_now_add=True)
    email = models.EmailField("Email", blank=False, null=False, unique=True)
    timeTried = models.IntegerField(default=0)

