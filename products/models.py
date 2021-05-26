from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200 , blank=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.category_name
    
class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.variant_name
    

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.color_name
    
    
class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.size_name


class Products(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "static/products")
    price = models.DecimalField(decimal_places=2 , max_digits=10)
    description = models.TextField()
    stock = models.IntegerField(default=100)
    
    quantity_type = models.ForeignKey(QuantityVariant, blank=True , null=True , on_delete=models.CASCADE)
    color_type = models.ForeignKey(ColorVariant, blank=True , null=True , on_delete=models.CASCADE)
    size_type = models.ForeignKey(SizeVariant, blank=True , null=True , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
class ProductImage(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "static/products")
