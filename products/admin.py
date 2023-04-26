from django.contrib import admin

from products.models import Product, Brand, Category

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
