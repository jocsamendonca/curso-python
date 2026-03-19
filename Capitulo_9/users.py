"""Classe que pode ser usada para representar um usuário"""

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
