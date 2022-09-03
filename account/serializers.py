
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(max_length=255)
    lastName = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['firstName', 'lastName', 'email', 'password']

class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class ConfirmTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255)
    userId=  serializers.IntegerField()
    class Meta:
        model = CustomUser
        fields = ['userId', 'token']

