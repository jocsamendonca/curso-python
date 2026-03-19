# 10.13 Dicionário de usuário
# 10.14

from pathlib import Path
import json

def get_stored_username(path):
    """Obtém o nome de usuário armazenado, se disponível"""
    if path.exists():
        contents = path.read_text()
        user_dictionary = json.loads(contents)
        return user_dictionary
    else:
        return None

def get_new_user(path):
    """Solicita um novo nome de usuário"""
    user_dictionary = {}
    user_dictionary['username'] = input("What is your name? ")
    user_dictionary['e-mail'] = input("Waht is your e-mail? ")
    user_dictionary['phone number'] = input("What is your phone number? ")
    contents = json.dumps(user_dictionary)
    path.write_text(contents)
    return user_dictionary

def greet_user():
    """Cumprimenta o usuário pelo nome"""
    path = Path('user_dictionary.json')
    user_dictionary = get_stored_username(path)
    if user_dictionary:
        print(f"Welcome! {user_dictionary['username']}.")
        answer = input("Is your username correct? (Y)es or (N)o? ")
        if answer == 'Y' or answer == 'y':
            print(f"Welcome back! {user_dictionary['username']}.")
            for key, value in user_dictionary.items():
                print(f"\t- {key}: {value}")
        else:
            user_dictionary = get_new_user(path)
            print(f"We'll remember you when come back, {user_dictionary}!")
        
greet_user()