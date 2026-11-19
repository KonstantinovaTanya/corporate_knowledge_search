
from fastapi import FastAPI

from app.core.config import (
    APP_NAME,
    APP_DESCRIPTION,
    APP_VERSION,
    APP_ENV
)


# Создаём приложение FastAPI
app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)


@app.get("/")
def read_root():
    return {
        "message": "Корпоративная система поиска знаний работает!",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV
    }
