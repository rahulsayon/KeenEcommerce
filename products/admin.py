from django.contrib import admin
from .models import Products,Category,SizeVariant,ColorVariant,QuantityVariant
# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(SizeVariant)
admin.site.register(ColorVariant)
admin.site.register(QuantityVariant)