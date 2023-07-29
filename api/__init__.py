from fastapi import APIRouter

from api.index import index_router
from api.product.product_api import product_router

router = APIRouter()
router.include_router(index_router, prefix="/index", tags=["Index"])
router.include_router(product_router, prefix="/product", tags=["Product"])

__all__ = ["router"]
