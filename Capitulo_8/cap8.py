'''

#8.1 Mensagem

def display_message():
    """Frase contando o que estou aprendendo neste capitulo"""
    print("Estou aprendo funções neste capítulo!")
    
display_message()

#8.2 Livro favorito

def favorite_book(title):
    print(f"Um dos meus livros favoritos é {title.title()}.")

favorite_book('curso intensivo de python')

#8.3 Camiseta

def make_shirt(tam, text):
    print(f"Você fez uma camisa tamanho {tam.upper()}. Com a seguinte mensagem: {text.title()}")

make_shirt('xg', 'reserva')
make_shirt(text='reserva', tam='xg')

#8.4 Camisetas grandes

def make_shirt(tam = 'xxg', text='eu amo python'):
    print(f"Você fez uma camisa tamanho {tam.upper()}. Com a seguinte mensagem: {text.title()}")

make_shirt()
make_shirt(tam='m')
make_shirt('g', 'Live free or die')

#8.5 Cidades

def describe_city(city, country='brazil'):
    print(f"\n{city.title()} fica no(a) {country.title()}.")

describe_city('fortaleza')
describe_city('porto alegre')
describe_city('porto', 'portugal')



#8.6 Nome de cidades

def city_country(city, country):
    c_country = f"{city.title()}, {country.title()}"
    return c_country

city = city_country('fortaleza', 'brasil')
print(city)

#8.7 Álbum

def make_album(nome, titulo, n_musicas = None):
    if n_musicas:
        album = {'artista': nome, 'titulo': titulo, 'numero_de_musicas': n_musicas}
    else:
        album = {'artista': nome, 'titulo': titulo}
    
    return album

album1 = make_album('The Beatles', "Sgt. Pepper's Lonely Hearts Club Band")
album2 = make_album('Led Zeppelin', 'IV')
album3 = make_album('Pink Floyd', 'The Dark Side of the Moon')
print(album1)
print(album2)
print(album3)

album4 = make_album('Pink Floyd', 'The Dark Side of the Moon', n_musicas=10)
print(album4)

#8.7 Álbum de usuários

while True:
    print("Informe o nome de seu artista e album preferidos: ")
    print("Digite 'q' a qualquer momento para sair. ")
    
    artista_usuario = input("Informe o nome do artista: ")
    if artista_usuario == 'q':
        break
    
    titulo_usuario = input("Informe o título do álbum: ")
    if titulo_usuario == 'q':
        break
    
    album_usuario = make_album(artista_usuario, titulo_usuario)
    print(f"\nSeus artistas e albuns favoritos: \n{album_usuario}")
    

#8.9 Mensagens

mensagens = ['Olá!', 'seja', 'bem vindo', 'ao', 'Curso Intensivo de', 'Python']

def show_messages(mensagens):
    for mensagem in mensagens:
        print(f"{mensagem}", end=" ")

#show_messages(mensagens)

#8.10 Enviando mensagens
sent_messages = []

def send_message(mensagens):
    while mensagens:
        current_message = mensagens.pop()
        print(f"{current_message}")
        sent_messages.append(current_message)

send_message(mensagens)
show_messages(mensagens)
show_messages(sent_messages)


#8.11 Mensagens arquivadas

def show_messages(mensagens):
    for mensagem in mensagens:
        print(f"{mensagem}", end=" ")


def send_message(mensagens):
    while mensagens:
        current_message = mensagens.pop()
        print(f"{current_message}")
        #sent_messages.append(current_message)
        sent_messages.insert(0,current_message)
        
mensagens = ['Olá!', 'seja', 'bem vindo', 'ao', 'Curso Intensivo de', 'Python']
sent_messages = []

send_message(mensagens[:])
show_messages(mensagens)
print()
#sent_messages.reverse()
show_messages(sent_messages)

'''
#8.12 Sanduíches

def make_sandwich(*toppings):
    print("\nMaking a sanwich with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('bacon', 'eggs')
make_sandwich('chiken')
make_sandwich('cheese', 'steak')

#8.13 Perfil de usuário
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('jocsã', 'mendonça', religiao= 'católico', profissao= 'bancário', formacao= 'contabilidade', estudando= 'analise e desenvolvimento de sistemas')
print(user_profile)

#8.14 Carros
def make_car(fab, mod, **car_info):
    car_info['fab'] = fab
    car_info['mod'] = mod
    return car_info

car = make_car('subaru', 'outback', color= 'blue', tow_package= True)
print(car)
car2 = make_car('volksWagen', 'virtus', color= 'black', tow_package= False)
print(car2)