import unittest
from unittest.mock import patch
from microservice.models.user import User, db

class TestUserModel(unittest.TestCase):

    @patch('microservice.models.user.db.session.add')
    @patch('microservice.models.user.db.session.commit')
    def test_add_user(self, mock_commit, mock_add):
        mock_add.return_value = None
        mock_commit.return_value = None
        user_name = 'testuser'
        user_email = 'test@example.com'
        mock_user = User(name=user_name, email=user_email)

        new_user  = User.add_user(mock_user)

        self.assertEqual(new_user, mock_commit.return_value)
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

    @patch('microservice.models.user.db.session.delete')
    @patch('microservice.models.user.db.session.commit')
    def test_delete_user(self, mock_commit, mock_delete):
        mock_commit.return_value = None
        mock_delete.return_value = None

        response= User.delete_user(13)
        
        self.assertEqual(response, mock_commit.return_value)
        mock_delete.assert_called_once()
        mock_commit.assert_called_once()

    @patch('microservice.models.user.db.session.commit')
    def test_update_user(self, mock_commit):
        mock_commit.return_value = None

        user = User(name='testuser', email='test@example.com')

        new_name = 'newusername'
        new_email = 'newemail@example.com'
        updated_user = User.update_user(user,new_name,new_email)

        self.assertEqual(updated_user, mock_commit.return_value)
        mock_commit.assert_called_once()
 
if __name__ == '__main__':
    unittest.main()