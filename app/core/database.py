import pyodbc

from app.core.config import (
    SQL_SERVER,
    SQL_DATABASE,
    SQL_DRIVER,
    SQL_TRUSTED_CONNECTION,
    SQL_TRUST_SERVER_CERTIFICATE
)


def get_connection():
    """Создаёт подключение к SQL Server."""

    connection_string = (
        f"DRIVER={{{SQL_DRIVER}}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"Trusted_Connection={SQL_TRUSTED_CONNECTION};"
        f"TrustServerCertificate={SQL_TRUST_SERVER_CERTIFICATE};"
    )

    return pyodbc.connect(connection_string)
