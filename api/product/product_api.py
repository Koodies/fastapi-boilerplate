from datetime import datetime
from fastapi import APIRouter
from typing import Union
from .product_request_schema import CreateProductRequestSchema
from .product_response_schema import (
    CreateProductResponseSchema,
    GetProductsResponseSchema,
    GetProductResponseSchema,
)
from app.product.product_model import Product
from app.product.product_service import (
    find_products,
    insert_product,
    find_product,
    delete_product,
)

product_router = APIRouter()


@product_router.get("/:id", status_code=200, response_model=GetProductResponseSchema)
def get_product(id):
    product = find_product()
    return product


@product_router.get("", status_code=200, response_model=GetProductsResponseSchema)
def get_products():
    products = find_products()
    return {"data": products}


@product_router.post(
    "",
    status_code=201,
    response_model=CreateProductResponseSchema,
)
async def create_product(request: CreateProductRequestSchema):
    product = Product(**request.dict(), createdOn=datetime.utcnow())
    insert_product(product)
    return product.dict(by_alias=True)
