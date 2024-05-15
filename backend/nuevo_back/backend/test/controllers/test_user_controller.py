import unittest
from flask import Flask, jsonify
from microservice.controllers import user_controller_blueprint  # Importa el módulo correcto
from unittest.mock import MagicMock, patch

patch_controller = 'microservice.controllers.user_controller.user_facade'
USERS_ROUTE = '/users'

class TestUserController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(user_controller_blueprint)
        
    def test_get_all_users(self):
        user_data = [
            {'id': 1, 'name': 'User1', 'email': 'user1@example.com'},
            {'id': 2, 'name': 'User2', 'email': 'user2@example.com'}
        ]
        
        user_facade = MagicMock()
        user_facade.get_all_users.return_value = user_data
        
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.get(USERS_ROUTE)
                data = response.get_json()

                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(data, list)
                self.assertEqual(len(data), 2)

                for user in user_data:
                    self.assertIn(user, data)


    def test_get_user(self):
        user_facade = MagicMock()
        user_facade.get_user_by_id.return_value = {'id': 1, 'name': 'Test', 'email': 'testUser@example.com'}
        
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.get('/users/1')
                data = response.get_json()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(data['name'], 'Test')
    
    def test_get_user_not_found(self):
        user_facade = MagicMock()
        user_facade.get_user_by_id.return_value = None  
        
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.get('/users/13')
                data = response.get_json()

                self.assertEqual(response.status_code, 404)
                self.assertEqual(data['message'], 'Usuario no encontrado')


    def test_create_user(self):
        user_facade = MagicMock()
        user_data = {'id': 1, 'name': 'Test', 'email': 'testEmail@example.com'}
        user_facade.create_user.return_value = user_data
        
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.post(USERS_ROUTE, json=user_data)
                data = response.get_json()

                self.assertEqual(response.status_code, 201)
                self.assertEqual(data['name'], 'Test')
    
    def test_create_data_missing_fields(self):
        user_facade = MagicMock()
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.post(USERS_ROUTE, json={})
                data = response.get_json()

                self.assertEqual(response.status_code, 400)
                self.assertEqual(data['message'], 'Name and email are required fields')


    def test_delete_user(self):
        user_facade = MagicMock()
        user_facade.delete_user.return_value = True
        
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.delete('/users/13')
                data = response.get_json()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(data['message'], 'User deleted successfully')

    def test_delete_user_not_found(self):
        user_facade = MagicMock()
        user_facade.delete_user.return_value = False  
        
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.delete('/users/10')
                data = response.get_json()

                self.assertEqual(response.status_code, 404)
                self.assertEqual(data['message'], 'User not found')


    def test_update_user(self):
        user_facade = MagicMock()
        user_facade.update_user.return_value = True
        
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.put('/users/1', json={'name': 'Updated', 'email': 'updated@example.com'})
                data = response.get_json()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(data['message'], 'Usuario actualizado exitosamente')
    
    def test_update_user_not_found(self):
        user_facade = MagicMock()
        user_facade.update_user.return_value = False  
        
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                response = client.put('/users/112', json={'name': 'Updated', 'email': 'updated@example.com'})
                data = response.get_json()

                self.assertEqual(response.status_code, 404)
                self.assertEqual(data['message'], 'Usuario no encontrado')

    def test_update_missing_fields(self):
        user_facade = MagicMock()
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                    response = client.put('/users/122', json={'name': 'Updated'})
                    data = response.get_json()

                    self.assertEqual(response.status_code, 400)
                    self.assertEqual(data['message'], 'Nombre y correo electrónico son obligatorios')

    def test_update_missing_data(self):
        user_facade = MagicMock()
        with patch(patch_controller, user_facade):
            with self.app.test_client() as client:
                    response = client.put('/users/132', json={})
                    data = response.get_json()

                    self.assertEqual(response.status_code, 400)
                    self.assertEqual(data['message'], 'Datos no proporcionados')

if __name__ == '__main__':
    unittest.main()