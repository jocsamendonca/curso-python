"""Classes que podem ser usadas para descrever os privilégios de um usuário"""

from users import User

class Privileges:
    """Privilégios de um usuário"""
    
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"\nO usuário possui os seguintes privilégios: {self.privileges}")
            
class Admin(User):
    """Define um usuário administrador"""
    
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()
