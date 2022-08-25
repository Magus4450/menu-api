from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    """ User Manager that knows how to create users via email instead of username """
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"
    
    email = models.EmailField("Email", blank=False, null=False, unique=True)
    imageUrl = models.TextField(default= "test", null=False, blank=False) 

    objects = CustomUserManager()
    def __str__(self):
        return self.first_name + ' ' + self.last_name