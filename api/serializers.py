from email.utils import localtime
from msilib.schema import SelfReg
from rest_framework import serializers
from .models import Restaurant, Category, Product
from django.utils.text import slugify
class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'slug', 'location')
        extra_kwargs = {'slug': {'read_only': True}}
    
    def create(self, validated_data):
        res = Restaurant.objects.create(
            name = validated_data['name'],
            location = validated_data['location'],
            slug = slugify(validated_data['name']),
        )
        res.save()
        return res


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')
        extra_kwargs = {'slug': {'read_only': True}}

    def create(self, validated_data):
        cat = Category.objects.create(
            name = validated_data['name'],
            slug = slugify(validated_data['name']),
        )
        cat.save()
        return cat
    

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'categoryId', 'restaurantId', 'name', 'price', 'description', 'imageUrl')

