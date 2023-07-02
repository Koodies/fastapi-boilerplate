
from fastapi import FastAPI



def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Koodies FastAPI Boilerplate",
        description="Koodies FastAPI Boilerplate",
        version="1.0.0",
    )
    return app_


app = create_app()