from rest_framework import serializers
#from yaml.serializer import Serializer
from .models import  Sale, Product, Permission, Group, User, Return
## create a serializers for api
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id', "username", 'role', "email"]

class ProductSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields = ["name", "description","price", 'total_stocks', "min_stocks_alert", "updated_at", "created_at"]
        read_only_fields = ["description"]
        date_hierarchy = 'updated_at'
        ordering = ('-created_at',)

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sale
        fields ="__all__"
        read_only_fields =["status_payment", "method_payment", 'quantity_sales', "date_sales"]

class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model=Return
        fields ="__all__"



