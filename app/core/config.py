
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

# Настройки подключения к SQL Server
SQL_SERVER = os.getenv(
    "SQL_SERVER",
    "DESKTOP-8ARU1LD"
)

SQL_DATABASE = os.getenv(
    "SQL_DATABASE",
    "CorporateKnowledgeSearch"
)

SQL_DRIVER = os.getenv(
    "SQL_DRIVER",
    "ODBC Driver 18 for SQL Server"
)

SQL_TRUSTED_CONNECTION = os.getenv(
    "SQL_TRUSTED_CONNECTION",
    "yes"
)

SQL_TRUST_SERVER_CERTIFICATE = os.getenv(
    "SQL_TRUST_SERVER_CERTIFICATE",
    "yes"
)
