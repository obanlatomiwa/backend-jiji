from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length= 120, default='location')

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Users.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()    

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.FloatField()
    description = models.TextField(max_length = 300)
    image = models.ImageField(upload_to="image")
    location = models.ForeignKey(Users, default='Location', on_delete=models.CASCADE)


class Buyer(models.Model):
    name = models.TextField(max_length=120)
    email = models.EmailField()
    location = models.TextField(max_length=120)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('product', 'email'),)
    
