from django.db import models

# Create your models here.


OPTIONS = (("ACTIVE","ACTIVE"), ("PENDING","PENDING"), ("DELETED","DELETED"))
DEFAULT_IMG = '\\media\\image\\test.jpg'
class Restaurant(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    slug = models.SlugField(max_length=225, null=False, blank=False)
    location = models.CharField(max_length=225, null=False, blank=False)
    imageUrl = models.TextField(default= DEFAULT_IMG, null=False, blank=False) 
    status = models.CharField(max_length=7, choices=OPTIONS)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    slug = models.SlugField(max_length=225, null=False, blank=False)
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    imageUrl = models.TextField(default= DEFAULT_IMG, null=False, blank=False) 
    status = models.CharField(max_length=7, choices=OPTIONS)


    def __str__(self):
        return self.name


class Product(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    description = models.TextField(default= DEFAULT_IMG, max_length=225, null=False, blank=False)
    imageUrl = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=7, choices=OPTIONS)

    def __str__(self):
        return self.name



