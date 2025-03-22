from rest_framework import serializers
#from yaml.serializer import Serializer
from .models import  Sale, Product, Permission, Group, User, Return
## create a serializers for api
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id', "username", 'role_choices', "email"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ["id", "name", "description","price_unit", 'total_stocks', "min_stocks_alert", "updated_at", "created_at"]
        date_hierarchy = 'updated_at'
        ordering = ('-created_at',)

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sale
        fields =['id', "product", "total_sales", "quantity_sales", 'total_sales', "date_sales", "status_payment", "method_payment"]
        read_only_fields =["status_payment", "method_payment", 'total_sales',"date_sales"]

class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model=Return
        fields ="__all__"



