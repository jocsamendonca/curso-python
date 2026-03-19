"""Classe que pode ser usada para criar um usuário admin"""

class User:
    """Modelando um usuário"""
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
    def describe_user(self):
        print(f"O usuário: {self.first_name.title()} {self.last_name.title()} está cadastrado com o e-mail: {self.email}")
    
    def greet_user(self):
        print(f"Olá {self.first_name.title()}! Seja bem vindo.")

class Privileges:
    
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges
    
    def show_privileges(self):
        print(f"\nO usuário possui os seguintes privilégios: {self.privileges}")
            
class Admin(User):
    
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        
        #self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()

# user = Admin('gabriel', 'mendonça', 'gabrielmendonca@gmail.com')
# user.privileges.show_privileges()