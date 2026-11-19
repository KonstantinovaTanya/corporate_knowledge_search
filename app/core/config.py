
import os
from dotenv import load_dotenv


# Загружаем настройки из файла .env
load_dotenv()


# Основные настройки приложения
APP_NAME = os.getenv(
    "APP_NAME",
    "Corporate Knowledge Search"
)

APP_DESCRIPTION = os.getenv(
    "APP_DESCRIPTION",
    "Система поиска знаний и ответов по внутренней документации"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "0.1.0"
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)
