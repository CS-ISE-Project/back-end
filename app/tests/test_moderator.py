import unittest
from unittest.mock import MagicMock
from fastapi import HTTPException, status
from app.services.moderator_service import get_all_moderators,get_moderator_by_email,get_moderator,create_moderator,update_moderator,delete_moderator,update_moderator_state
from app.models.moderator import UpdateModeratorModel
from app.schemas.moderator import Moderator


class TestGetAllMods(unittest.TestCase): 
    def test_get_all_mods_with_mods(self):
        # Mock the database session
        mock_db_with_mods = MagicMock()
        # Mock the query method to return some admins
        mock_db_with_mods.query.return_value.all.return_value = [
            Moderator(id=1, first_name="Moderator1_first", last_name="anything", email="example@example.com",password="123",is_active=False),
            Moderator(id=2, first_name="Moderator2_first", last_name="anything", email="example2@example.com",password="123",is_active=False)
        ]

        # Call the function
        mods_with_mods = get_all_moderators(mock_db_with_mods)

        # Assert that the function returns the correct admins
        self.assertEqual(len(mods_with_mods), 2)
        self.assertEqual(mods_with_mods[0].id, 1)
        self.assertEqual(mods_with_mods[1].id, 2)
        self.assertEqual(mods_with_mods[0].first_name, "Moderator1_first")
        self.assertEqual(mods_with_mods[1].first_name, "Moderator2_first")

    def test_get_all_admins_with_no_admins(self):
        # Mock the database session
        mock_db_no_mods = MagicMock()
        # Mock the query method to return an empty list
        mock_db_no_mods.query.return_value.all.return_value = []

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            get_all_moderators(mock_db_no_mods)

        # Assert that the exception has the expected status code
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        
class TestGetModeratorByEmail(unittest.TestCase):
    def test_get_moderator_by_email_exists(self):
        # Mock the database session
        mock_db = MagicMock()
        
        # Mock the query method to return a moderator with the specified email
        mock_db.query().filter().first.return_value = Moderator(id=1, first_name="Moderator1_first", last_name="anything", email="moderator@example.com",password="123",is_active=False)

        # Call the function
        moderator = get_moderator_by_email("moderator@example.com", mock_db)

        # Assert that the function returns the correct moderator
        self.assertEqual(moderator.id, 1)
        self.assertEqual(moderator.email, "moderator@example.com")

    def test_get_moderator_by_email_not_exists(self):
        # Mock the database session
        mock_db = MagicMock()
        
        # Mock the query method to return None (moderator not found)
        mock_db.query().filter().first.return_value = None

        # Call the function
        moderator = get_moderator_by_email("nonexistent@example.com", mock_db)

        # Assert that the function returns None (moderator not found)
        self.assertIsNone(moderator)        
        
class TestGetModerator(unittest.TestCase):
    def test_get_moderator_exists(self):
        # Mock the database session
        mock_db = MagicMock()
        
        # Mock the query method to return a moderator with the specified id
        mock_db.query().filter().first.return_value = Moderator(id=1, first_name="Moderator1_first", last_name="Moderator1_last", email="moderator@example.com",password="123",is_active=False)

        # Call the function
        moderator = get_moderator(1, mock_db)

        # Assert that the function returns the correct moderator
        self.assertEqual(moderator.id, 1)
        self.assertEqual(moderator.email, "moderator@example.com")
        self.assertEqual(moderator.last_name, "Moderator1_last")

    def test_get_moderator_not_exists(self):
        # Mock the database session
        mock_db = MagicMock()
        
        # Mock the query method to return None (moderator not found)
        mock_db.query().filter().first.return_value = None

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            get_moderator(999, mock_db)

        # Assert that the exception has the expected status code and detail message
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, "Moderator with id 999 not found")

class TestCreateModerator(unittest.TestCase):
    def test_create_moderator_success(self):
        # Mock the ModeratorModel instance
        mod_model = Moderator(id=1, first_name="Test", last_name="Moderator", email="test@example.com",password="123",is_active=False)

        # Mock the database session
        mock_db = MagicMock()

        # Call the function
        created_mod = create_moderator(mod_model, mock_db)

        # Assert that the function returns the created moderator
        self.assertEqual(created_mod.first_name, "Test")
        self.assertEqual(created_mod.last_name, "Moderator")
        self.assertEqual(created_mod.email, "test@example.com")

class TestUpdateModerator(unittest.TestCase):
    def test_update_moderator_success(self):
        # Mock the database session
        mock_db = MagicMock()

        existing_mod = Moderator(id=1, first_name="Moderator1_first", last_name="anything", email="example@example.com",password="123",is_active=False)
        # Mock the UpdateModeratorModel instance
        updated_mod_model = UpdateModeratorModel(
            first_name="Updated",
            last_name="Moderator",
            email="updated@example.com"
        )

        # Mock the query method to return an existing moderator
        mock_db.query.return_value.filter.return_value.first.return_value = existing_mod

        # Call the function
        updated_mod = update_moderator(1, updated_mod_model, mock_db)
        # Assert that the function returns the updated moderator
        self.assertEqual(updated_mod.first_name, "Updated")
        self.assertEqual(updated_mod.last_name, "Moderator")
        self.assertEqual(updated_mod.email, "updated@example.com")

    def test_update_moderator_not_found(self):
        # Mock the UpdateModeratorModel instance
        updated_mod_model = UpdateModeratorModel(first_name="Updated", last_name="Moderator", email="updated@example.com")

        # Mock the database session to return None (moderator not found)
        mock_db = MagicMock()
        mock_db.query().filter().first.return_value = None

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            update_moderator(999, updated_mod_model, mock_db)

        # Assert that the exception has the expected status code and detail message
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, "Moderator with id 999 not found")
        
class TestUpdateIsActive(unittest.TestCase):
    def test_update_isActive_success(self):
        # Mock the database session
        mock_db = MagicMock()

        existing_mod = Moderator(id=1, first_name="Moderator1_first", last_name="anything", email="example@example.com",password="123",is_active=False)
        # Mock the query method to return an existing moderator
        mock_db.query().filter().first.return_value = existing_mod

        # Call the function
        updated_mod = update_moderator_state(1, True, mock_db)
        # Assert that the function returns the updated moderator
        self.assertIsInstance(updated_mod, Moderator)
        self.assertEqual(updated_mod.id, 1)
        self.assertEqual(updated_mod.is_active, True)

    def test_update_isActive_not_found(self):
        # Mock the database session to return None (moderator not found)
        mock_db = MagicMock()
        mock_db.query().filter().first.return_value = None

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            update_moderator_state(999, True, mock_db)

        # Assert that the exception has the expected status code and detail message
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, "Moderator with id 999 not found")

class TestDeleteModerator(unittest.TestCase):
    def test_delete_moderator_success(self):
        # Mock the database session
        mock_db = MagicMock()

        # Mock the query method to return an existing moderator
        mock_db.query().filter().first.return_value = Moderator(id=1, first_name="Moderator1_first", last_name="anything", email="example@example.com",password="123",is_active=False),

        # Call the function
        response = delete_moderator(1, mock_db)

        # Assert that the function returns the expected response
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_moderator_not_found(self):
        # Mock the database session to return None (moderator not found)
        mock_db = MagicMock()
        mock_db.query().filter().first.return_value = None

        # Call the function and assert that it raises an exception
        with self.assertRaises(HTTPException) as context:
            delete_moderator(999, mock_db)

        # Assert that the exception has the expected status code and detail message
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, "Moderator with id 999 not found")
