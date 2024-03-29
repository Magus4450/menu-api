from django.db import models
from django.utils import timezone

OPTIONS = (("ACTIVE","ACTIVE"), ("PENDING","PENDING"), ("DELETED","DELETED"))
DEFAULT_IMG = '\\media\\image\\test.jpg'
class Restaurant(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    slug = models.SlugField(max_length=225, null=False, blank=False)
    location = models.CharField(max_length=225, null=False, blank=False)
    imageUrl = models.TextField(default= DEFAULT_IMG, null=False, blank=False) 
    status = models.CharField(max_length=7, choices=OPTIONS, default=("PENDING", "PENDING"))
    timeCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    slug = models.SlugField(max_length=225, null=False, blank=False)
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    imageUrl = models.TextField(default= DEFAULT_IMG, null=False, blank=False) 
    status = models.CharField(max_length=7, choices=OPTIONS, default=("PENDING", "PENDING"))
    timeCreated = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


class Product(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    description = models.TextField(default= DEFAULT_IMG, max_length=225, null=False, blank=False)
    imageUrl = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=7, choices=OPTIONS, default=("PENDING", "PENDING"))
    timeCreated = models.DateTimeField(default=timezone.now)
    productType = models.CharField(max_length=12, 
        choices=(("VEG","VEG"), ("NON_VEG","NON_VEG"), ("CONTAINS_EGG", "CONTAINS_EGG")), default=("VEG", "VEG")
    )


    def __str__(self):
        return self.name



