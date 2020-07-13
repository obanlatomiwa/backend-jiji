from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    location = models.CharField(max_length= 120)

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    description = models.TextField(max_length = 300)
    image = models.ImageField()
    location = models.CharField(max_length= 120)
    
