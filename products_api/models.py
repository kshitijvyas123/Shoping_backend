from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

    

class Products(models.Model):
    class ProductSize(models.TextChoices):   
        SMALL = 'S'
        MEDIUM = 'M'
        LARGE = 'L'
        EXTRA_L = 'XL'
        DOUBLE_XL = 'XXL'

    class ProductColor(models.TextChoices):
        RED = 'RED'
        WHITE = 'WHITE'
        BLACK = 'BLACK'
        GREY = 'GREY'

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(max_length = 1000)
    price = models.IntegerField(max_length=4, default=0)
    qty = models.IntegerField(default= None)
    reviews = models.IntegerField(default= 0)
    availability = models.CharField(max_length=10, default='Available')
    brand = models.CharField(max_length=100, default= None, null=False)
    category = models.CharField(max_length=100, default= None)
    sku = models.CharField(max_length=10 , default= None)
    size = models.CharField(choices=ProductSize.choices, max_length=10, default='S')
    previousPrice= models.IntegerField(max_length=4, default=0)
    color= models.CharField(choices=ProductColor.choices,max_length=10, default='RED')

    def __str__(self):
        return self.name


class RegisterUser(models.Model):
    username = models.CharField(max_length = 40, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 20)
    # Add custom fields here, if needed

    def __str__(self):
        return self.username
