from django.contrib import admin
from .models import  Product, User, Sale, Return
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Return)