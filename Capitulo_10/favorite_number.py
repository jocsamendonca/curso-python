# Exercício 10.12
from pathlib import Path
import json

path = Path('favoriteNumber.json')

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"Eu sei seu número favorito! É {favorite_number}.")

else:
    favorite_number = input("Qual é seu número favorito? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)