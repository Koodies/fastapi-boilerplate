from fastapi import APIRouter

from api.index import index_router
from api.product.product_api import product_router
from api.shop.shop_api import shop_router

router = APIRouter()
router.include_router(index_router, prefix="/index", tags=["Index"])
router.include_router(product_router, prefix="/product", tags=["Product"])
router.include_router(shop_router, prefix="/shop", tags=["Shop"])

__all__ = ["router"]
