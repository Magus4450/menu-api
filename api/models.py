from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    slug = models.SlugField(max_length=225, null=False, blank=False)
    location = models.CharField(max_length=225, null=False, blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    slug = models.SlugField(max_length=225, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    description = models.TextField(max_length=225, null=False, blank=False)
    image_url = models.ImageField(upload_to='products', null=False, blank=False)

    def __str__(self):
        return self.name

