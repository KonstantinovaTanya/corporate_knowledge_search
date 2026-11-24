from enum import Enum


class UserRole(str, Enum):
    """Роли пользователей системы."""

    EMPLOYEE = "employee"
    DEPARTMENT_HEAD = "department_head"
    ADMIN = "admin"


class AccessLevel(str, Enum):
    """Уровни доступа к документам."""

    ALL = "all"
    DEPARTMENT = "department"
    ADMIN = "admin"