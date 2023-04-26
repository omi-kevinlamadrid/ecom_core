from base.models import BaseModel, BaseManager
from django.db import models


class Category(BaseModel):
    name = models.CharField(max_length=128, verbose_name="Name")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    objects = BaseManager()


class Brand(BaseModel):
    name = models.CharField(max_length=128, verbose_name="Name")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    objects = BaseManager()


class Product(BaseModel):
    name = models.CharField(max_length=64, verbose_name="Name")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    is_active = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    objects = BaseManager()