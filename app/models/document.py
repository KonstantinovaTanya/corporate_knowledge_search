from pydantic import BaseModel

from app.models.enums import AccessLevel

class Document(BaseModel):
    """Модель документа системы."""

    id: str
    title: str
    department: str
    access_level: AccessLevel
    author_id: str
    content: str