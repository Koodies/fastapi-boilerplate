from fastapi import APIRouter
from api.shop.shop_response_schema import GetShopResponseSchema, GetShopsResponseSchema

shop_router = APIRouter()

shops = [
    {
        "name": "Shop 1",
        "description": "Shop 1 description",
        "is_deleted": False,
        "created_at": "2021-10-10T00:00:00.000Z",
    }
]


@shop_router.get("/:id", status_code=200, response_model=GetShopResponseSchema)
def get_shop(id):
    return shops[0]


@shop_router.get("", status_code=200, response_model=GetShopsResponseSchema)
def get_shops():
    return {"data": shops}
