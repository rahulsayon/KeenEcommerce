from django.db.models import fields
from rest_framework import serializers
from .models import *
from products.serializers import ProductSerializer

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        

class CartItemsSerializers(serializers.ModelSerializer):
    product = ProductSerializer()
    cart= CartSerializers()
    class Meta:
        model = CartItems
        fields = '__all__'
        
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        
