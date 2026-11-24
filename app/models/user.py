from pydantic import BaseModel

from app.models.enums import UserRole


class User(BaseModel):
    """Модель пользователя системы."""

    id: str
    role: UserRole
    department: str