#9.10 Importando Restaurant
    
"""Classe que pode ser usada para representar um restaurante"""

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
 