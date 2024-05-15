from ..models import User

class UserRepository:
    def get_all_users(self):
        return User.query.all()

    def get_user(self, user_id):
        user =  User.query.get(user_id)
        return user if user else None
    
    def create_user(self, _name, _email):
        user = User(name=_name, email=_email)
        User.add_user(user)
        return user
    
    def delete_user(self, _user_id):
        user = User.query.get(_user_id)
        if user:
            User.delete_user(user)
            return True
        
    def update_user(self, _user_id, _name, _email):
        user = User.query.get(_user_id)
        if user:
            User.update_user(user,_name, _email)
            return True

        
    