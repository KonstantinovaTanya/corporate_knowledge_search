
import unittest

from app.models.user import User
from app.models.enums import UserRole
from app.services.search_service import search_documents

# Проверка поиска с ограничением доступа
class TestSearchService(unittest.TestCase):

    def setUp(self):
        self.employee = User(
            id="test_employee",
            role=UserRole.EMPLOYEE,
            department="HR"
        )

        self.department_head = User(
            id="test_head",
            role=UserRole.DEPARTMENT_HEAD,
            department="Finance"
        )

        self.admin = User(
            id="test_admin",
            role=UserRole.ADMIN,
            department="Administrative"
        )

    def check_access(self, results, department):
        for document in results:
            self.assertIn(
                document["access_level"],
                ["all", "department"]
            )

            if document["access_level"] == "department":
                self.assertEqual(
                    document["department"],
                    department
                )

    def test_employee_search_access(self):
        results = search_documents(self.employee, "доступ")

        self.assertTrue(results, "Поиск не вернул документов")

        self.check_access(results, "HR")

    def test_department_head_search_access(self):
        results = search_documents(self.department_head, "бюджет")

        self.assertTrue(results, "Поиск не вернул документов")

        self.check_access(results, "Finance")

    def test_admin_search_access(self):
        results = search_documents(self.admin, "доступ")

        self.assertTrue(results, "Поиск не вернул документов")

        access_levels = {
            document["access_level"]
            for document in results
        }

        departments = {
            document["department"]
            for document in results
        }

        self.assertIn("admin", access_levels)
        self.assertIn("department", access_levels)
        self.assertIn("all", access_levels)

        self.assertGreater(
            len(departments),
            1,
            "Администратор должен видеть документы разных подразделений"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
