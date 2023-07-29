from typing import Optional
from pydantic import BaseModel, Field


class CreateProductRequestSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
