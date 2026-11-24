from app.models.user import User
from app.models.document import Document
from app.models.enums import UserRole, AccessLevel


def can_view_document(user: User, document: Document) -> bool:
    """Проверяет, может ли пользователь просматривать документ."""

    role = user.role
    department = user.department
    access_level = document.access_level

    if role == UserRole.ADMIN:
        return True

    if access_level == AccessLevel.ADMIN:
        return False

    if access_level == AccessLevel.ALL:
        return True

    if access_level == AccessLevel.DEPARTMENT:
        return department == document.department

    return False


def can_edit_document(user: User, document: Document) -> bool:
    """Проверяет, может ли пользователь изменять документ."""

    role = user.role
    department = user.department

    if role == UserRole.ADMIN:
        return True

    if document.access_level == AccessLevel.ADMIN:
        return False

    if role == UserRole.DEPARTMENT_HEAD:
        return department == document.department

    if role == UserRole.EMPLOYEE:
        return user.id == document.author_id

    return False


def can_delete_document(user: User, document: Document) -> bool:
    """Проверяет, может ли пользователь удалять документ."""

    role = user.role
    department = user.department

    if role == UserRole.ADMIN:
        return True

    if document.access_level == AccessLevel.ADMIN:
        return False

    if role == UserRole.DEPARTMENT_HEAD:
        return department == document.department

    if role == UserRole.EMPLOYEE:
        return user.id == document.author_id

    return False


def can_create_document(user: User, document_department: str, access_level: AccessLevel) -> bool:
    """Проверяет, может ли пользователь создавать документ."""

    role = user.role
    department = user.department

    if role == UserRole.ADMIN:
        return True

    if access_level == AccessLevel.ADMIN:
        return False

    if role in [UserRole.EMPLOYEE, UserRole.DEPARTMENT_HEAD]:
        return department == document_department

    return False
