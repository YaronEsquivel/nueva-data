import unittest
import json
from microservice.services import UserService
from unittest.mock import patch

class UserServiceTestCase(unittest.TestCase):

    @patch('microservice.services.user_service.UserRepository')
    def test_get_all_users(self, mock_user_repository):
        mock_user_repository.return_value.get_all_users.return_value = [
            {
                "user_id": 1, 
                "name": "test1", 
                "email": "test1@mail.com"
            },
            {
                "user_id": 2, 
                "name": "test2", 
                "email": "test2@mail.com"
            }
        ]

        user_service = UserService()
        users = user_service.get_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0]['name'], 'test1')
        self.assertEqual(users[0]['email'], 'test1@mail.com')
        self.assertEqual(users[1]['name'], 'test2')
        self.assertEqual(users[1]['email'], 'test2@mail.com')


    @patch('microservice.services.user_service.UserRepository')
    def test_user_by_id(self, mock_user_repository):
        mock_user = {
                "user_id": 13, 
                "name": "test13", 
                "email": "test13@mail.com"
            }
        mock_user_repository.return_value.get_user.return_value = mock_user

        user_service = UserService()
        user = user_service.get_user_by_id(13)

        self.assertEqual(user, mock_user)
    

    @patch('microservice.services.user_service.UserRepository')
    def test_create_user(self, mock_user_repository):
        new_user = {
            "user_id": 3,
            "name": "NewUser",
            "email": "newuser@mail.com"
        }
        
        mock_user_repository.return_value.create_user.return_value = new_user

        user_service = UserService()
        created_user = user_service.create_user(new_user['name'],new_user['email'])
  
        self.assertEqual(created_user['user_id'], new_user['user_id'])
        self.assertEqual(created_user['name'], new_user["name"])
        self.assertEqual(created_user['email'], new_user["email"])


    @patch('microservice.services.user_service.UserRepository')
    def test_delete_user(self, mock_user_repository):
        user_id_to_delete = 1
        
        mock_user_repository.return_value.delete_user.return_value = True

        user_service = UserService()
        result = user_service.delete_user(user_id_to_delete)

        self.assertTrue(result)


    @patch('microservice.services.user_service.UserRepository')
    def test_update_user(self, mock_user_repository):
        updated_user = {
            "user_id": 3,
            "name": "UpdatedUser",
            "email": "updateduser@mail.com"
        }

        mock_user_repository.return_value.update_user.return_value = updated_user

        user_service = UserService()
        new_updated_user = user_service.update_user(updated_user['user_id'], updated_user['name'], updated_user['email'])

        self.assertEqual(updated_user['user_id'], new_updated_user['user_id'])
        self.assertEqual(updated_user["name"], updated_user["name"])
        self.assertEqual(updated_user["email"], updated_user["email"])


if __name__ == '__main__':
    unittest.main()