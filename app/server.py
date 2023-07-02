
from fastapi import FastAPI
from api import router

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Koodies FastAPI Boilerplate",
        description="Koodies FastAPI Boilerplate",
        version="1.0.0",
    )
    init_routers(app_)
    return app_


app = create_app()