#9.1 Restaurante
'''

class Restaurant:
    """Simples tentativa de modelar um restaurantes"""
    
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """ Descreve um restaurante"""
        print(f"{self.restaurant_name.title()} é um restaurante que serve comida {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} está aberto!")
        
restaurant = Restaurant('La Spezia', 'italiana')
print(f"O nome do restaurante é {restaurant.restaurant_name}.")
print(f"O tipo de cozinha é {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2 Três restaurantes
restaurant1 = Restaurant('Dom Parente', 'brasileira')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('Boteco do Chefe', 'nordestina')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('Nori', 'japonesa')
restaurant3.describe_restaurant()

#9.3 Usuários

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
        
user0 = User('jocsã', 'mendonça', 'jocsamendonca@gmail.com')
user0.describe_user()
user0.greet_user()



#9.4 Pessoas Atendidas
    #9.1 Copy
class Restaurant:
    """Simples tentativa de modelar um restaurantes"""
    
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """ Descreve um restaurante"""
        print(f"{self.restaurant_name.title()} é um restaurante que serve comida {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} está aberto!")
        
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number
          
restaurant = Restaurant('La Spezia', 'italiana')
restaurant.describe_restaurant()
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)



#9.5 Tentativas de login
    #9.3
class User:
    """Modelando um usuário"""
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"O usuário: {self.first_name.title()} {self.last_name.title()} está cadastrado com o e-mail: {self.email}")
    
    def greet_user(self):
        print(f"Olá {self.first_name.title()}! Seja bem vindo.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Você realizou {self.login_attempts} tentativa(s) de login!")
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Tentativas de login resetadas!")
      
user = User('jocsã', 'mendonça', 'jocsamendonca@gmail.com')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
print(user.login_attempts)



#9.6 Sorveteria

    #9.1 Restaurante

class Restaurant:
    """Simples tentativa de modelar um restaurantes"""
    
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """ Descreve um restaurante"""
        print(f"{self.restaurant_name.title()} é um restaurante que serve {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} está aberto!")
        
# restaurant = Restaurant('La Spezia', 'italiana')
# print(f"O nome do restaurante é {restaurant.restaurant_name}.")
# print(f"O tipo de cozinha é {restaurant.cuisine_type}")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
    
        self.flavors = f"\n\tFlocos. \n\tCreme. \n\tDoce de leite. \n\tChocolate Belga."
        
    def get_flavors(self):
        print(f"\nLista de sabores de sorvetes: \n{self.flavors}")

my_ice_cream = IceCreamStand('J&G Sorvetes', 'sorvetes')
my_ice_cream.describe_restaurant()
my_ice_cream.get_flavors()



#9.7 Admin
    #9.3 Usuários

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
        
# user0 = User('jocsã', 'mendonça', 'jocsamendonca@gmail.com')
# user0.describe_user()
# user0.greet_user()

class Admin(User):
    
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print(f"\nO administrador, {self.first_name.title()}, possui os seguintes privilégios: ")
        for self.privilege in self.privileges:
            print(f"\t - {self.privilege}")
user1 = Admin('jorge', 'mendonça', 'jorgemendonca@gmail.com')
user1.show_privileges()



#9.8 Privilégios

#9.7 Admin
    #9.3 Usuários

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

user = Admin('gabriel', 'mendonça', 'gabrielmendonca@gmail.com')
user.privileges.show_privileges()



#9.9 Trocar bateria

class Car:
    """Simples tentativa de representar um carro"""
    
    def __init__(self, make, model, year):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reanding = 0
    
    def get_descriptive_name(self):
        """Retorna ..."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reanding} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reanding:
            self.odometer_reanding = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reanding += miles

class Battery:
    
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
    
class EletricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


#9.13 Dados
from random import randint

class Die:
    
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        lado = randint(1, self.sides)
        print(f"\n\t{lado}")
    

dado = Die()
dado.roll_die()

dado10 = Die(10)
dado10.roll_die()
dado20 = Die(20)
dado20.roll_die()

'''

#9.14 Loteria
'''

import random
import string

# Gerando números aleatórios
numeros_aleatorios = random.sample(range(1, 101), 10)

# Gerando letras aleatórias
letras_aleatorias = random.sample(string.ascii_lowercase, 5)

# Combinando números e letras em uma tupla
tupla_aleatoria = tuple(numeros_aleatorios + letras_aleatorias)

# print(tupla_aleatoria)
# Bilhete premiado
sorteado = random.choice(tupla_aleatoria)
print(f"Qualquer bilhete que tenha a sequencia {sorteado}")
'''
from random import choices, sample

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

# Com repetição dos valores
# sorteado = choices(lista, k=4)
# print(sorteado)

#Sem repetição dos valores
# sorteado2 = sample(lista, k=4)
# print(f"{sorteado2}")

#9.15 Análise de loteria

my_ticket = [1, 5, 10, 'a']
sorteado2 = []
sorteios = 0

while my_ticket != sorteado2:
    sorteado2 = sample(lista, k=4)
    sorteios += 1

print(f"\nNumero de sorteios necessários para vencer: {sorteios}. \n{my_ticket}\n{sorteado2}")
