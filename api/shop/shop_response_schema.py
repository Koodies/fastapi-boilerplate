from pydantic import BaseModel

class Shop(BaseModel):
    name: str
    description: str
    is_deleted: bool = False
    created_at: str


class GetShopsResponseSchema(BaseModel):
    data: list[Shop]

class GetShopResponseSchema(Shop):
    pass
