import unittest
from unittest.mock import MagicMock
from fastapi import HTTPException, status
from app.services.admin_service import get_all_admins,get_admin,get_admin_by_email,create_admin,update_admin,delete_admin
from app.models.admin import CompleteAdminModel,AdminModel,UpdateAdminModel
from app.schemas.admin import Admin


class TestGetAllAdmins(unittest.TestCase):
    def test_get_all_admins_with_admins(self):
        mock_db_with_admins = MagicMock()
        mock_db_with_admins.query.return_value.all.return_value = [
            Admin(id=1, first_name="Admin1_first", last_name="Admin1_last", email="admin1@example.com",password="133"),
            Admin(id=2, first_name="Admin2_first", last_name="Admin2_last", email="admin2@example.com",password="133")
        ]

        admins_with_admins = get_all_admins(mock_db_with_admins)

        self.assertEqual(len(admins_with_admins), 2)
        self.assertEqual(admins_with_admins[0].id, 1)
        self.assertEqual(admins_with_admins[1].id, 2)
        self.assertEqual(admins_with_admins[0].first_name, "Admin1_first")
        self.assertEqual(admins_with_admins[1].first_name, "Admin2_first")

    def test_get_all_admins_with_no_admins(self):
        mock_db_no_admins = MagicMock()
        mock_db_no_admins.query.return_value.all.return_value = []

        with self.assertRaises(HTTPException) as context:
            get_all_admins(mock_db_no_admins)

        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)

class TestGetAdmin(unittest.TestCase):
    def test_get_admin_found(self):
        mock_db_with_admin = MagicMock()
        mock_db_with_admin.query.return_value.filter.return_value.first.return_value = Admin(
            id=1, first_name="Admin1_first", last_name="Admin1_last", email="admin1@example.com",password="1223"
        )

        admin = get_admin(1, mock_db_with_admin)

        self.assertEqual(admin.id, 1)
        self.assertEqual(admin.first_name, "Admin1_first")

    def test_get_admin_not_found(self):
        mock_db_no_admin = MagicMock()
        mock_db_no_admin.query.return_value.filter.return_value.first.return_value = None

        with self.assertRaises(HTTPException) as context:
            get_admin(1, mock_db_no_admin)

        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        
class TestGetAdminByEmail(unittest.TestCase):
    def test_get_admin_by_email_found(self):
        mock_db_with_admin = MagicMock()
        mock_db_with_admin.query.return_value.filter.return_value.first.return_value = Admin(
            id=1, first_name="Admin1_first", last_name="Admin1_last", email="admin1@example.com",password="12323"
        )

        admin = get_admin_by_email("admin1@example.com", mock_db_with_admin)

        self.assertEqual(admin.id, 1)
        self.assertEqual(admin.first_name, "Admin1_first")
        self.assertEqual(admin.last_name, "Admin1_last")
        self.assertEqual(admin.email, "admin1@example.com")

    def test_get_admin_by_email_not_found(self):
        mock_db_no_admin = MagicMock()
        mock_db_no_admin.query.return_value.filter.return_value.first.return_value = None

        admin = get_admin_by_email("admin@example.com", mock_db_no_admin)
        self.assertIsNone(admin)
        
class TestCreateAdmin(unittest.TestCase):
    def test_create_admin_successfully(self):
        mock_db = MagicMock()

        admin_model = AdminModel(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="password123"
        )

        created_admin = create_admin(admin_model, mock_db)

        self.assertEqual(created_admin.first_name, "John")
        self.assertEqual(created_admin.last_name, "Doe")
        self.assertEqual(created_admin.email, "john.doe@example.com")

        mock_db.add.assert_called_once_with(created_admin)
        mock_db.commit.assert_called_once()

class TestUpdateAdmin(unittest.TestCase):
    def test_update_admin_successfully(self):
        mock_db = MagicMock()

        existing_admin = Admin(id=1, first_name="John", last_name="Doe", email="john.doe@example.com",password="1235")

        updated_admin_model = UpdateAdminModel(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com"
        )

        mock_db.query.return_value.filter.return_value.first.return_value = existing_admin

        updated_admin = update_admin(1, updated_admin_model, mock_db)

        self.assertEqual(updated_admin.first_name, "Jane")
        self.assertEqual(updated_admin.last_name, "Doe")
        self.assertEqual(updated_admin.email, "jane.doe@example.com")

        mock_db.commit.assert_called_once()

    def test_update_admin_not_found(self):
        mock_db = MagicMock()

        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        updated_admin_model = UpdateAdminModel(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com"
        )

        with self.assertRaises(HTTPException) as context:
            update_admin(1, updated_admin_model, mock_db)

        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        
class TestDeleteAdmin(unittest.TestCase):
    def test_delete_admin_successfully(self):
        mock_db = MagicMock()

        admin_to_delete = Admin(id=1, first_name="John", last_name="Doe", email="john.doe@example.com",password="1256")

        mock_db.query.return_value.filter.return_value.first.return_value = admin_to_delete

        response = delete_admin(1, mock_db)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        mock_db.delete.assert_called_once_with(admin_to_delete)
        mock_db.commit.assert_called_once()

    def test_delete_admin_not_found(self):
        mock_db = MagicMock()

        mock_db.query.return_value.filter.return_value.first.return_value = None

        with self.assertRaises(HTTPException) as context:
            delete_admin(1, mock_db)

        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)