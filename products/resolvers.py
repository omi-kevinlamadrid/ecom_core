import graphene
from products.models import Product, Category, Brand
from products.types import ProductType, CategoryType, BrandType


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_categories = graphene.List(CategoryType)
    all_brands = graphene.List(BrandType)

    product = graphene.Field(ProductType, product_id=graphene.Int(), required=True)
    category = graphene.Field(CategoryType, category_id=graphene.Int(), required=True)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_products(self, info):
        return Product.objects.select_related('category', 'brand',).all()

    def resolve_product(self, info, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def resolve_all_categories(self, info):
        return Category.objects.all()

    def resolve_category(self, info, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    def resolve_all_brands(self, info):
        return Brand.objects.all()

    def resolve_brand(self, info, brand_id):
        try:
            return Brand.objects.get(id=brand_id)
        except Brand.DoesNotExist:
            return None


    def resolve_category_by_name(self, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
