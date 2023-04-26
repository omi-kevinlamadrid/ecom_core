import graphene
from products.types import ProductType, ProductInput, ProductUpdateInput, CategoryInput, CategoryType, \
    CategoryUpdateInput, BrandType, BrandUpdateInput
from products.models import Category, Brand, Product
import decimal


class CreateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):

        product = Product.objects.create(
            name=product_data.name,
            description=product_data.description,
            price=decimal.Decimal(product_data.price)
        )

        return CreateProduct(product=product)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True, description="ID of Product")
        input_data = ProductUpdateInput(required=True, description="Fields required to update")

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id=None, input_data=None):
        try:
            product = Product.objects.get(id=id)
            product.name = input_data.name
            product.description = input_data.description
            product.price = decimal.Decimal(input_data.price)
            product.save()
            return UpdateProduct(product=product)
        except Product.DoesNotExists():
            return UpdateProduct(product=None)


# class UpdateProductActivation(graphene.Mutation):
#     class Arguments:
#         ids = graphene.List(Product)
#         is_active = graphene.Enum()
#
#     product = graphene.Field(ProductType)
#     @staticmethod
#     def mutate(root, info, ids=[], is_active=False):
#         for item_id in ids:
#             try:
#                 product = Product.objects.get(id=item_id)
#                 product.name = is_active
#                 product.save()
#                 return
#             except Product.DoesNotExists():
#                 return UpdateProduct(product=None)


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id=None):
        product_instance = Product.objects.get(id=id)
        if product_instance:
            return None
        product_instance.delete()
        return None


#Category
class CreateCategory(graphene.Mutation):
    class Arguments:
        category_data = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, category_data=None):
        category = Category.objects.create(
            name=category_data.name,
            description=category_data.description,
        )
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True, description="ID of Category")
        input_data = CategoryUpdateInput(required=True, description="Fields required to update")

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, id=None, input_data=None):
        try:
            category = Category.objects.get(id=id)
            category.name = input_data.name
            category.description = input_data.description
            category.save()
            return UpdateProduct(category=category)
        except Category.DoesNotExists():
            return UpdateCategory(category=None)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, id=None):
        category_instance = Category.objects.get(id=id)
        if category_instance:
            return None
        category_instance.delete()
        return None


class CreateBrand(graphene.Mutation):
    class Arguments:
        brand_data = CategoryInput(required=True)

    brand = graphene.Field(BrandType)

    @staticmethod
    def mutate(root, info, brand_data=None):
        brand = Brand.objects.create(
            name=brand_data.name,
            description=brand_data.description,
        )
        return CreateBrand(brand=brand)


class UpdateBrand(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True, description="ID of Category")
        input_data = BrandUpdateInput(required=True, description="Fields required to update")

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, id=None, input_data=None):
        try:
            brand = Category.objects.get(id=id)
            brand.name = input_data.name
            brand.description = input_data.description
            brand.save()
            return UpdateProduct(brand=brand)
        except Brand.DoesNotExists():
            return UpdateBrand(brand=None)


class DeleteBrand(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(BrandType)

    @staticmethod
    def mutate(root, info, id=None):
        brand_instance = Brand.objects.get(id=id)
        if brand_instance:
            return None
        brand_instance.delete()
        return None

