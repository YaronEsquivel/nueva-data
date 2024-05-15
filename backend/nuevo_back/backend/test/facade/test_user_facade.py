import unittest
from unittest.mock import Mock
from microservice.facade import UserFacade
from unittest.mock import patch
from microservice.dtos import UserDTO

class TestUserFacade(unittest.TestCase):
    def test_get_all_users(self):
        mock_user_service = Mock()
        mock_user_data = [
            UserDTO(user_id=13, name="User13", email="User13@example.com"),
            UserDTO(user_id=14, name="User14", email="User14@example.com"),
        ]
        mock_user_service.get_all_users.return_value = mock_user_data

        user_facade = UserFacade()
        user_facade.user_service = mock_user_service

        result = user_facade.get_all_users()

        expected_result = [
            {"user_id": 13, "name": "User13", "email": "User13@example.com"},
            {"user_id": 14, "name": "User14", "email": "User14@example.com"},
        ]
        self.assertEqual(result, expected_result)


    def test_get_user_by_id(self):
        mock_user_service = Mock()
        mock_user_data = UserDTO(user_id=1, name="nameUser", email="emailUser@example.com")
        mock_user_service.get_user_by_id.return_value = mock_user_data

        user_facade = UserFacade()
        user_facade.user_service = mock_user_service

        result = user_facade.get_user_by_id(1)

        expected_result = {
            "user_id": 1,
            "name": "nameUser",
            "email": "emailUser@example.com"
        }
        self.assertEqual(result, expected_result)


    def test_create_user(self):
        user = {
            "user_id": 1,
            "name": "NewUser",
            "email": "newuser@example.com"
        }

        mock_user_service = Mock()
        mock_created_user = UserDTO(user_id=user["user_id"], name=user["name"], email=user["email"])
        mock_user_service.create_user.return_value = mock_created_user

        user_facade = UserFacade()
        user_facade.user_service = mock_user_service

        result = user_facade.create_user(user["name"], user["email"])

        expected_result = {
            "user_id": 1,
            "name": "NewUser",
            "email": "newuser@example.com"
        }

        self.assertEqual(result, expected_result)


    @patch('microservice.facade.user_facade.UserService')
    def test_delete_user(self, mock_user_service):
        user_id_to_delete = 1
        
        mock_user_service.return_value.delete_user.return_value = True

        user_facade = UserFacade()
        user_facade.user_service = mock_user_service

        result = user_facade.delete_user(user_id_to_delete)

        self.assertTrue(result)


    @patch('microservice.facade.user_facade.UserService')
    def test_update_user(self, mock_user_service):
        user_id = 1
        updated_name = "UpdatedName"
        updated_email = "updated@example.com"

        mock_user_service.return_value.update_user.return_value = True

        user_facade = UserFacade()
        user_facade.user_service = mock_user_service

        result = user_facade.update_user(user_id, updated_name, updated_email)

        self.assertTrue(result)

    
    def test_user_to_dict(self):
        user_id = 1
        user_name = "TestUser"
        user_email = "test@example.com"

        mock_user = Mock()
        mock_user.user_id = user_id
        mock_user.name = user_name
        mock_user.email = user_email

        user_facade = UserFacade()
        result = user_facade._user_to_dict(mock_user)

        expected_result = {
            "user_id": user_id,
            "name": user_name,
            "email": user_email
        }
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()