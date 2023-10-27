from pydantic import BaseModel
from app.product.product_model import Product


class GetProductsResponseSchema(BaseModel):
    data: list[Product]


class GetProductResponseSchema(Product):
    pass


class CreateProductResponseSchema(Product):
    pass
