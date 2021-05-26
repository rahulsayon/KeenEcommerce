from rest_framework import serializers
from .models import Category, Products, QuantityVariant


        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    quantity_type = QuantitySerializer()
    class Meta:
        model = Products
        fields = '__all__'