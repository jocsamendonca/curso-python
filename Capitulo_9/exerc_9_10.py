#9.10 Importando Restaurant
from restaurant import Restaurant

restaurant = Restaurant('Bodega Cariri', 'Nordestina')
print(f"O restaurant {restaurant.restaurant_name} serve comida {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()
