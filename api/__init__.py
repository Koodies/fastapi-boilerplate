from fastapi import APIRouter

from api.index import index_router

router = APIRouter()
router.include_router(index_router, prefix="/index", tags=["Index"])


__all__ = ["router"]
