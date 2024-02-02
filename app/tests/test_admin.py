import unittest
from unittest.mock import MagicMock
from fastapi import HTTPException, status
from app.services.admin_service import get_all_admins,get_admin,get_admin_by_email,create_admin,update_admin,delete_admin
from app.models.admin import CompleteAdminModel,AdminModel,UpdateAdminModel

class TestGetAllAdmins(unittest.TestCase):
    def test_get_all_admins_with_admins(self):
        # Mock the database session
        mock_db_with_admins = MagicMock()
        # Mock the query method to return some admins
        mock_db_with_admins.query.return_value.all.return_value = [
            CompleteAdminModel(id=1, first_name="Admin1_first", last_name="Admin1_last", email="admin1@example.com"),
            CompleteAdminModel(id=2, first_name="Admin2_first", last_name="Admin2_last", email="admin2@example.com")
        ]

        # Call the function
        admins_with_admins = get_all_admins(mock_db_with_admins)

        # Assert that the function returns the correct admins
        self.assertEqual(len(admins_with_admins), 2)
        self.assertEqual(admins_with_admins[0].id, 1)
        self.assertEqual(admins_with_admins[1].id, 2)
        self.assertEqual(admins_with_admins[0].first_name, "Admin1_first")
        self.assertEqual(admins_with_admins[1].first_name, "Admin2_first")

    def test_get_all_admins_with_no_admins(self):
        # Mock the database session
        mock_db_no_admins = MagicMock()
        # Mock the query method to return an empty list
        mock_db_no_admins.query.return_value.all.return_value = []

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            get_all_admins(mock_db_no_admins)

        # Assert that the exception has the expected status code
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)

class TestGetAdmin(unittest.TestCase):
    def test_get_admin_found(self):
        # Mock the database session
        mock_db_with_admin = MagicMock()
        # Mock the query method to return an admin
        mock_db_with_admin.query.return_value.filter.return_value.first.return_value = CompleteAdminModel(
            id=1, first_name="Admin1_first", last_name="Admin1_last", email="admin1@example.com"
        )

        # Call the function
        admin = get_admin(1, mock_db_with_admin)

        # Assert that the function returns the correct admin
        self.assertEqual(admin.id, 1)
        self.assertEqual(admin.first_name, "Admin1_first")

    def test_get_admin_not_found(self):
        # Mock the database session
        mock_db_no_admin = MagicMock()
        # Mock the query method to return None
        mock_db_no_admin.query.return_value.filter.return_value.first.return_value = None

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            get_admin(1, mock_db_no_admin)

        # Assert that the exception has the expected status code
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        
class TestGetAdminByEmail(unittest.TestCase):
    def test_get_admin_by_email_found(self):
        # Mock the database session
        mock_db_with_admin = MagicMock()
        # Mock the query method to return an admin
        mock_db_with_admin.query.return_value.filter.return_value.first.return_value = CompleteAdminModel(
            id=1, first_name="Admin1_first", last_name="Admin1_last", email="admin1@example.com"
        )

        # Call the function
        admin = get_admin_by_email("admin1@example.com", mock_db_with_admin)

        # Assert that the function returns the correct admin
        self.assertEqual(admin.id, 1)
        self.assertEqual(admin.first_name, "Admin1_first")
        self.assertEqual(admin.last_name, "Admin1_last")
        self.assertEqual(admin.email, "admin1@example.com")

    def test_get_admin_by_email_not_found(self):
        # Mock the database session
        mock_db_no_admin = MagicMock()
        # Mock the query method to return None
        mock_db_no_admin.query.return_value.filter.return_value.first.return_value = None

        # Call the function and assert that it returns None
        admin = get_admin_by_email("admin@example.com", mock_db_no_admin)
        self.assertIsNone(admin)
        
class TestCreateAdmin(unittest.TestCase):
    def test_create_admin_successfully(self):
        # Mock the database session
        mock_db = MagicMock()

        # Create an AdminModel instance to represent the admin being created
        admin_model = AdminModel(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="password123"
        )

        # Call the function
        created_admin = create_admin(admin_model, mock_db)

        # Assert that the function returns the created admin
        self.assertEqual(created_admin.first_name, "John")
        self.assertEqual(created_admin.last_name, "Doe")
        self.assertEqual(created_admin.email, "john.doe@example.com")
        # Add more assertions as needed

        # Assert that the add and commit methods were called on the database session
        mock_db.add.assert_called_once_with(created_admin)
        mock_db.commit.assert_called_once()

class TestUpdateAdmin(unittest.TestCase):
    def test_update_admin_successfully(self):
        # Mock the database session
        mock_db = MagicMock()

        # Create an Admin instance representing the admin in the database
        existing_admin = CompleteAdminModel(id=1, first_name="John", last_name="Doe", email="john.doe@example.com")

        # Create an UpdateAdminModel instance representing the updated data
        updated_admin_model = UpdateAdminModel(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com"
        )

        # Mock the query method to return the existing admin
        mock_db.query.return_value.filter.return_value.first.return_value = existing_admin

        # Call the function
        updated_admin = update_admin(1, updated_admin_model, mock_db)

        # Assert that the function returns the updated admin
        self.assertIsInstance(updated_admin, CompleteAdminModel)
        self.assertEqual(updated_admin.first_name, "Jane")
        self.assertEqual(updated_admin.last_name, "Doe")
        self.assertEqual(updated_admin.email, "jane.doe@example.com")
        # Add more assertions as needed

        # Assert that the commit method was called on the database session
        mock_db.commit.assert_called_once()

    def test_update_admin_not_found(self):
        # Mock the database session
        mock_db = MagicMock()

        # Mock the query method to return None (admin not found)
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        updated_admin_model = UpdateAdminModel(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com"
        )

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            update_admin(1, updated_admin_model, mock_db)

        # Assert that the exception has the expected status code
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        
class TestDeleteAdmin(unittest.TestCase):
    def test_delete_admin_successfully(self):
        # Mock the database session
        mock_db = MagicMock()

        # Create an Admin instance representing the admin to be deleted
        admin_to_delete = CompleteAdminModel(id=1, first_name="John", last_name="Doe", email="john.doe@example.com")

        # Mock the query method to return the admin to be deleted
        mock_db.query.return_value.filter.return_value.first.return_value = admin_to_delete

        # Call the function
        response = delete_admin(1, mock_db)

        # Assert that the function returns a successful response
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert that the delete method was called on the database session
        mock_db.delete.assert_called_once_with(admin_to_delete)
        mock_db.commit.assert_called_once()

    def test_delete_admin_not_found(self):
        # Mock the database session
        mock_db = MagicMock()

        # Mock the query method to return None (admin not found)
        mock_db.query.return_value.filter.return_value.first.return_value = None

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            delete_admin(1, mock_db)

        # Assert that the exception has the expected status code
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)