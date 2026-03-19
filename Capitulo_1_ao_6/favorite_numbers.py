#6.2
'''
favorite_numbers = {'jorge': 4, 'gabriel': 2, 'jocsa': 1, 'nilce': 5, 'cinete': 31}

for name, number in favorite_numbers.items():
    print(f'O número favorito de {name.title()} é: {number}')
'''

#6.10 Uma lista em um dicionário

favorite_numbers = {'jorge': [4, 21, 2, 19], 'gabriel': [2, 21, 4, 21], 'jocsa': [1, 11, 4, 90], 'nilce': [5, 9, 89], 'cinete': [31, 10, 58]}

for name, numbers in favorite_numbers.items(): # acessando as chaves  e valores do dicionário
    print(f'\n{name.title()}`s favorite numbers are:') #imprimindo as chaves
    for number in numbers: #acessando a lista
        print(f'\t{number}')#imprimindo os itens da lista