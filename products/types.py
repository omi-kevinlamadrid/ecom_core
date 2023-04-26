import graphene
from graphene_django import DjangoObjectType
from products.models import Category, Brand, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class BrandType(DjangoObjectType):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'description', )


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class BrandInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()


class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    price = graphene.Float()


class ProductUpdateInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    price = graphene.Float()


class CategoryUpdateInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()


class BrandUpdateInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
