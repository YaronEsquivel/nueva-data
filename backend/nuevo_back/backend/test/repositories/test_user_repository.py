import unittest
from unittest.mock import patch
from microservice.repositories import UserRepository  # Importa la clase UserRepository desde tu módulo
from microservice import create_app

app = create_app()

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Limpia el contexto de la aplicación después de las pruebas
        self.app_context.pop()

    @patch('microservice.repositories.User.query')
    def test_get_all_users(self, mock_query):
        mock_users = [
            {
                "user_id": 13, 
                "name": "test13", 
                "email": "test13@mail.com"
            }, 
            {
                "user_id": 13, 
                "name": "test13", 
                "email": "test13@mail.com"
            }
        ]
        mock_query.all.return_value = mock_users

        user_repo = UserRepository()
        users = user_repo.get_all_users()

        self.assertEqual(users, mock_users)


    @patch('microservice.repositories.User.query')
    def test_get_user(self, mock_query):
        # Simula el comportamiento de la consulta de SQLAlchemy
        user_data = {'user_id': 20, 'name': 'User Test', 'email': 'UserTest1@example.com'}
        mock_query.get.return_value = user_data

        user_repo = UserRepository()
        user = user_repo.get_user(1)

        self.assertEqual(user, user_data)


    @patch('microservice.repositories.User.query')
    def test_get_user_not_found(self, mock_query):
        mock_query.get.return_value = None

        user_repo = UserRepository()
        user = user_repo.get_user(1)

        self.assertIsNone(user) 


    @patch('microservice.repositories.User.add_user')
    def test_create_user(self, mock_add_user):
        user_data = {'user_id': 33, 'name': 'UserTest', 'email': 'UserTest@example.com'}
        mock_add_user.return_value = user_data

        user_repo = UserRepository()
        new_user = user_repo.create_user('UserTest', 'UserTest@example.com')

        self.assertEqual(new_user.name, user_data['name'])
        self.assertEqual(new_user.email, user_data['email'])


    @patch('microservice.repositories.User.query')
    @patch('microservice.repositories.User.delete_user')
    def test_delete_user(self, mock_delete_user, mock_get_user):
        # Simula el comportamiento de User.query.get y User.delete_user
        mock_get_user.return_value = {'user_id': 33, 'name': 'test', 'email': 'test@example.com'}
        mock_delete_user.return_value = True

        user_repo = UserRepository()
        result = user_repo.delete_user(33)
        self.assertTrue(result)
    
    @patch('microservice.repositories.User.query')
    def test_delete_user_not_found(self, mock_query):
        user_id = 67

        mock_query.get.return_value = None

        user_repo = UserRepository()
        result = user_repo.delete_user(user_id)

        self.assertFalse(result)


    @patch('microservice.repositories.User.query')
    @patch('microservice.repositories.User.update_user')
    def test_update_user(self, mock_update_user, mock_get_user):
       
        user_data = {'user_id': 22, 'name': 'user', 'email': 'user@example.com'}
        mock_get_user.return_value = user_data
        mock_update_user.return_value = True

        user_repo = UserRepository()
        result = user_repo.update_user(22, 'New Name', 'new@example.com')

        self.assertTrue(result)


    @patch('microservice.repositories.User.query')
    def test_update_user_not_found(self, mock_query):
        user_id = 67

        mock_query.get.return_value = None

        user_repo = UserRepository()
        result = user_repo.update_user(user_id, 'New User', 'newuser@mail.com')

        self.assertFalse(result)
    
        
if __name__ == '__main__':
    unittest.main()