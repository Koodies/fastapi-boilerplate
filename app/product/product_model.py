from datetime import datetime
from typing import Optional
from app.library.pydantic import PydanticObjectId
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    name: str
    description: Optional[str] = None
    price: float
    is_deleted: bool = Field(default=False, alias="isDeleted")
    created_on: datetime = Field(alias="createdOn")
