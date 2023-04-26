import graphene
from products.mutation import CreateProduct, \
    UpdateProduct, DeleteProduct, CreateCategory, UpdateCategory, DeleteCategory, DeleteBrand, UpdateBrand, CreateBrand
from products.resolvers import Query


class AllMutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    delete_brand = DeleteBrand.Field()
    update_brand = UpdateBrand.Field()
    create_brand = CreateBrand.Field()





schema = graphene.Schema(query=Query, mutation=AllMutation)