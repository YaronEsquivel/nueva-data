from ..dtos import UserDTO
from ..services import UserService

class UserFacade:
    def __init__(self):
        self.user_service = UserService()

    def get_all_users(self):
        users = self.user_service.get_all_users()
        return [self._user_to_dict(user) for user in users]
    
    def get_user_by_id(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        return self._user_to_dict(user) if user else None
    
    def create_user(self, name, email):
        user = self.user_service.create_user(name, email)
        return self._user_to_dict(user)
    
    def delete_user(self, user_id):
        user = UserService()
        return user.delete_user(user_id)
    
    def update_user(self, user_id, name, email):
        user = UserService()
        return user.update_user(user_id,name, email)
    
    def _user_to_dict(self, user):
        return UserDTO(user.user_id, user.name, user.email).__dict__