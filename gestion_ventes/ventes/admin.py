from django.contrib import admin
from .models import  Product, User, Sale
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Sale)