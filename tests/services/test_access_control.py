
import unittest

from app.models.user import User
from app.models.document import Document
from app.models.enums import AccessLevel

from app.services.access_control import (
    can_view_document,
    can_edit_document,
    can_delete_document,
    can_create_document
)

# Проверка логики прав
class TestAccessControl(unittest.TestCase):

    def setUp(self):
        self.employee = User(
            id="user_1",
            role="employee",
            department="IT"
        )

        self.department_head = User(
            id="head_1",
            role="department_head",
            department="IT"
        )

        self.admin = User(
            id="admin_1",
            role="admin",
            department="Administrative"
        )

        self.own_document = Document(
            id="DOC001",
            title="Мой документ",
            department="IT",
            access_level="department",
            author_id="user_1",
            content="Тестовое содержимое"
        )

        self.other_document = Document(
            id="DOC002",
            title="Документ другого сотрудника",
            department="IT",
            access_level="department",
            author_id="user_2",
            content="Тестовое содержимое"
        )

        self.foreign_document = Document(
            id="DOC003",
            title="Документ другого подразделения",
            department="HR",
            access_level="department",
            author_id="user_3",
            content="Тестовое содержимое"
        )

        self.admin_document = Document(
            id="DOC101",
            title="Административный доступ",
            department="IT",
            access_level="admin",
            author_id="admin_1",
            content="Тестовое содержимое"
        )

    # Проверка просмотра

    def test_employee_can_view_department_document(self):
        self.assertTrue(
            can_view_document(self.employee, self.other_document)
        )

    def test_employee_cannot_view_foreign_department_document(self):
        self.assertFalse(
            can_view_document(self.employee, self.foreign_document)
        )

    def test_employee_cannot_view_admin_document(self):
        self.assertFalse(
            can_view_document(self.employee, self.admin_document)
        )

    def test_admin_can_view_any_document(self):
        self.assertTrue(
            can_view_document(self.admin, self.admin_document)
        )

    def test_department_head_cannot_view_foreign_department_document(self):
        self.assertFalse(
            can_view_document(self.department_head, self.foreign_document)
        )

    def test_employee_can_view_all_document(self):
        document = Document(
            id="DOC004",
            title="Общий документ",
            department="HR",
            access_level="all",
            author_id="user_3",
            content="Общедоступное содержимое"           
        )
    
        self.assertTrue(
            can_view_document(self.employee, document)
        )
    
    
    def test_department_head_can_view_all_document(self):
        document = Document(
            id="DOC005",
            title="Общий документ",
            department="HR",
            access_level="all",
            author_id="user_3",
            content="Общедоступное содержимое"
        )
                
        self.assertTrue(
            can_view_document(self.department_head, document)
        )    

    # Проверка изменения

    def test_employee_can_edit_own_document(self):
        self.assertTrue(
            can_edit_document(self.employee, self.own_document)
        )

    def test_employee_cannot_edit_other_document(self):
        self.assertFalse(
            can_edit_document(self.employee, self.other_document)
        )

    def test_department_head_can_edit_department_document(self):
        self.assertTrue(
            can_edit_document(self.department_head, self.other_document)
        )

    def test_department_head_cannot_edit_foreign_document(self):
        self.assertFalse(
            can_edit_document(self.department_head, self.foreign_document)
        )

    def test_admin_can_edit_any_document(self):
        self.assertTrue(
            can_edit_document(self.admin, self.foreign_document)
        )

    def test_employee_cannot_edit_admin_document(self):
        self.assertFalse(
            can_edit_document(self.employee, self.admin_document)
        )


    def test_department_head_cannot_edit_admin_document(self):
        self.assertFalse(
            can_edit_document(self.department_head, self.admin_document)
        )

    # Проверка удаления

    def test_employee_can_delete_own_document(self):
        self.assertTrue(
            can_delete_document(self.employee, self.own_document)
        )

    def test_employee_cannot_delete_other_document(self):
        self.assertFalse(
            can_delete_document(self.employee, self.other_document)
        )

    def test_department_head_can_delete_department_document(self):
        self.assertTrue(
            can_delete_document(self.department_head, self.other_document)
        )

    def test_admin_can_delete_any_document(self):
        self.assertTrue(
            can_delete_document(self.admin, self.foreign_document)
        )

    def test_employee_cannot_delete_admin_document(self):
        self.assertFalse(
            can_delete_document(self.employee, self.admin_document)
        )

    def test_department_head_cannot_delete_admin_document(self):
        self.assertFalse(
            can_delete_document(self.department_head, self.admin_document)
        )

    # Проверка создания

    def test_employee_can_create_document_in_own_department(self):
        self.assertTrue(
            can_create_document(self.employee, "IT", AccessLevel.DEPARTMENT)
        )

    def test_employee_cannot_create_document_in_foreign_department(self):
        self.assertFalse(
            can_create_document(self.employee, "HR", AccessLevel.DEPARTMENT)
        )

    def test_department_head_can_create_document_in_own_department(self):
        self.assertTrue(
            can_create_document(self.department_head, "IT", AccessLevel.DEPARTMENT)
        )

    def test_admin_can_create_document_in_any_department(self):
        self.assertTrue(
            can_create_document(self.admin, "HR", AccessLevel.DEPARTMENT)
        )

    def test_employee_cannot_create_admin_document(self):
        self.assertFalse(
            can_create_document(self.employee, "IT", AccessLevel.ADMIN)
        )

    def test_department_head_cannot_create_admin_document(self):
        self.assertFalse(
            can_create_document(self.department_head, "IT", AccessLevel.ADMIN)  
        )
    
    

if __name__ == "__main__":
    unittest.main()
