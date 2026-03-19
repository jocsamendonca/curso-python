#5.8
'''
names = ["admin", "Jaden", "Guilherme", "Jorge", "Gabriel"]

for name in names:
    if name == "admin":
        print(f"Olá administrador, gostaria de ver um relatório de status?")
    else:
        print(f"Olá {name}, obrigado por fazer login novamente.")
'''
#5.9  
'''
names = []

if names:
    for name in names:
        if name == "admin":
            print(f"Olá administrador, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {name}, obrigado por fazer login novamente.")
else:
    print("Não há usuários cadastrados no momento.")
'''

#5.10
'''

print()
print("=" * 70)
print()
current_users = ["admin", "Jaden", "Guilherme", "Jorge", "GABRIEL"]
new_users = ["jorge", "Gabriel", "Jocsã", "Nilce", "Cinete"]

#current_users = [current_user.lower() for current_user in current_users]
#new_users = [new_user.lower() for new_user in new_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user.capitalize()} já está registrado como usuário atual.")
    else:
        print(f"{new_user.capitalize()} é um novo usuário e será adicionado à lista de usuários.")

#5.11
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(f"\n{number}st")
    elif number == 2:
        print(f"\n{number}nd")
    elif number == 3:
        print(f"\n{number}rd")
    else:
        print(f"\n{number}th")
'''
# 6.3
'''
glossario = {'loop':'Eh um tipo de repeticao para percorrer um serie de valores',
             'lista': 'Uma das forma de armazenar um conjunto de dados', 
             'variavel': 'armazrna uma informacao de forma nao definitiva',
             'funcao': 'uma rotina que executa um trecho de codigo com parametros',
             'wrapper':'involucro, envolve uma variavel para aplicar um metodo', 
             'metodos': 'rotinas ou funcoes que podem ser chamadas em algumas classes',
             'classe': 'modelo de estrutura de dados', 
             }
#print(f'\nloop: \n\t{glossario["loop"]}')

for k, v in glossario.items():
    print(f'{k}: \n\t{v}\n')
'''
# 6.5
'''
rios = {'nile': 'egypt', 'amazonas': 'brasil', 'sao francisco': 'brasil(nordeste)'}

for rio, pais in rios.items():
    print(f"O {rio} atravessa o {pais}")

for rio in sorted(rios.keys()):
    print(f"{rio}")

for pais in sorted(rios.values()):
    print(f"{pais}")

'''
# 6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
lista_participantes = ['jen', 'phil', 'jorge', 'gabriel']

for nome in lista_participantes:
    if nome not in favorite_languages.keys():
        print(f'{nome.title()} gostaria de participar da nossa pesquisa?') 
    else:
        print(f'{nome.title()} obrigado por ter participado da pesquisa!')
    
