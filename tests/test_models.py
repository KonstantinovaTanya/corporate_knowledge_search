import unittest
from pydantic import ValidationError

from app.models.user import User
from app.models.document import Document


class TestModels(unittest.TestCase):

    def test_create_user(self):
        user = User(
            id="user_1",
            role="employee",
            department="IT"
        )

        self.assertEqual(user.role, "employee")

    def test_invalid_user_role(self):
        with self.assertRaises(ValidationError):
            User(
                id="user_1",
                role="manager",
                department="IT"
            )

    def test_create_document(self):
        document = Document(
            id="DOC101",
            title="Порядок предоставления административного доступа",
            department="IT",
            access_level="admin",
            author_id="admin_1",
            content="Тестовое содержимое"
        )

        self.assertEqual(document.access_level, "admin")

    def test_invalid_access_level(self):
        with self.assertRaises(ValidationError):
            Document(
                id="DOC102",
                title="Тестовый документ",
                department="IT",
                access_level="private",
                author_id="user_1",
                content="Тест"
            )


if __name__ == "__main__":
    unittest.main()