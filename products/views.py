from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response
from products.models import Category, Products
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductView(APIView):
    def get(self,request):
        category = self.request.query_params.get("category")
        if category:
            queryset= Products.objects.filter(category__category_name=category)
        else:
            queryset = Products.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)
    
class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        return Response({ "success" : "Authenticate successfully" })
    


    
    