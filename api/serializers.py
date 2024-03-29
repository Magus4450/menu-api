
from django.utils.text import slugify
from rest_framework import serializers

from .models import Category, Product, Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'slug', 'location',
                  'imageUrl', 'status', 'timeCreated')
        extra_kwargs = {'slug': {'read_only': True},
                        'timeCreated': {'read_only': True}}

    def create(self, validated_data):
        res = Restaurant.objects.create(
            name=validated_data['name'],
            location=validated_data['location'],
            slug=slugify(validated_data['name']),
            imageUrl=validated_data['imageUrl'],
            status=validated_data['status'],
        )
        res.save()
        return res


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'restaurantId',
                  'imageUrl', 'status', 'timeCreated')
        extra_kwargs = {'slug': {'read_only': True},
                        'timeCreated': {'read_only': True}}

    def create(self, validated_data):
        cat = Category.objects.create(
            name=validated_data['name'],
            slug=slugify(validated_data['name']),
            restaurantId=validated_data['restaurantId'],
            imageUrl=validated_data['imageUrl'],
            status=validated_data['status'],

        )

        cat.save()
        return cat


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'categoryId', 'restaurantId', 'name', 'price',
                  'description', 'imageUrl', 'status', 'timeCreated', 'productType')
        extra_kwargs = {'timeCreated': {'read_only': True}}

class UploadSerializer(serializers.Serializer):
    image = serializers.FileField()
    type = serializers.CharField(max_length=100)
