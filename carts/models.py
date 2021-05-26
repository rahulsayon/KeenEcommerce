from functools import total_ordering
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from products.models import Category, Products

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price  = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.user.username) 
    
    

class CartItems(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price  = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.user.username) 
    
@receiver(pre_save , sender=CartItems)
def correct_price(sender,**kwargs):
    cart_item = kwargs["instance"]
    price_of_product = Products.objects.get(id=cart_item.product.id)
    cart_item.price = cart_item.quantity * float(price_of_product.price)
    total_cart_items = CartItems.objects.filter(user=cart_item.user)
    cart_item.total_items = len(total_cart_items)
    cart = Cart.objects.get(id=cart_item.cart.id)
    cart.total_price = cart_item.price
    cart.save()
    
    

class Orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount = models.FloatField(default=0,blank=True)
    is_paid = models.BooleanField(default=False,blank=True)
    order_id = models.CharField(max_length=100,blank=True)
    payment_id = models.CharField(max_length=100,blank=True)
    payment_signature = models.CharField(max_length=100,blank=True)
    
    
class OrderedItems(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)


