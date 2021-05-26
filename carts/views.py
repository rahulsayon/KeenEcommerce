from django.db.models.expressions import OrderBy
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import *
from products.models import Products
from .serializer import *

class CartView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user,ordered = False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializers(queryset,many=True)
        return Response(serializer.data)
              
    
    def post(self,request):
        data = request.data
        user = request.user
        cart,_ = Cart.objects.get_or_create(user=user,ordered=False)
        product = Products.objects.get(id=data.get("product"))
        price = product.price
        quantity = data.get("quantity")
        cart_item = CartItems(user=user,product=product,cart=cart,quantity=quantity,price=price)
        cart_item.save()     
        
        total_price = 0
        cart_item = CartItems.objects.filter(user=user,cart=cart.id)
        for item in cart_item:
            total_price  += item.price
        cart.total_price = total_price
        cart.save()
         
        return Response({ "success" : "Item Added successfully"})
    
    def update(self,request):
        data = request.data
        cartItems = CartItems.objects.get(id=data.get("id"))
        quantity = data.get("quantity")
        cartItems.quantity += quantity
        cartItems.save()
        return Response({"success" : "Item Updated"})
    
    def delete(self,request):
        user = request.user
        data = request.data
        
        cart_item = CartItems.objects.get(id=data.get("id"))
        cart_item.delete()
        
        cart = Cart.objects.filter(user=user,ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializers(queryset,many=True)
        return Response(serializer.data)
    
    
class OrderAPI(APIView):
    def get(self,request):
        queryset = Orders.objects.filter(user=request.user)
        serializer = OrderSerializers(queryset,many=True)
        return Response(serializer.data)