
from fastapi import FastAPI

from app.core.config import (
    APP_NAME,
    APP_DESCRIPTION,
    APP_VERSION,
    APP_ENV
)

from app.api.documents import router as documents_router


app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)


app.include_router(documents_router)


@app.get("/")
def read_root():
    return {
        "message": "Корпоративная система поиска знаний работает!",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV
    }
