from django.contrib import admin

# Register your models here.
from .models import Product, Buyer, Users

admin.site.register(Product)
admin.site.register(Buyer)
admin.site.register(Users)