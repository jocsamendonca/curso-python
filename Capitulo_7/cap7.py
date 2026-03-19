
'''

#7.1 Aluguel de carro
carro = input("Que tipo de carro gostaria de alugar: ")
print(f"Vejamos se consigo encontrar um {carro} para você.")

#7.2 Reservas em restaurante
lugares = input("Quantos lugares a mesa o Sr. precisa? ")
lugares = int(lugares)

if lugares > 8:
    print("Será necessário aguardar por uma mesa.")
else:
    print("A mesa já está disponível.")

#7.2 Mútiplos de 10
#%%
numero = int(input("Informe um número: "))
if numero % 10 == 0:
    print(f"{numero} é mútiplo de 10.")
else:
    print(f"{numero} não é mútiplo de 10.") 
#%%    

#7.4 Ingredientes de pizza

ingrediente = ''
while ingrediente != 'quit':
    ingrediente = input("Iinforme o ingrediente que deseja adiconar a Pizza ou 'quit' para sair: ")
    if ingrediente == 'quit':
        break
    else:
        print(f"Voce adicionou {ingrediente} a pizza.")


#7.5 Ingressos de cinema
op = ''
while op != 'quit':
    
    idade = int(input("\nInforme a sua idade para saber o valor do ingresso para o cinema: "))
    
    if idade > 12:
        print("O ingresso custa US$15")
    elif idade >= 3:
        print("O preco do ingresso e US$10")
    else:
        print("Entrada gratuita! ")
        
    op = str(input( "\n(Pressione Enter para continuar ou Digite 'quit' para sair.)")).lower()
    if op == 'quit':
        break



#7.6 Ingressos de cinema
active = True

while active:
    
    idade = int(input("\nInforme a sua idade para saber o valor do ingresso para o cinema: "))
    
    if idade > 12:
        print("O ingresso custa US$15")
    elif idade >= 3:
        print("O preco do ingresso e US$10")
    else:
        print("Entrada gratuita! ")
        
    mensage = str(input( "\n(Pressione Enter para continuar ou Digite 'quit' para sair.)")).lower()
    if mensage == 'quit':
        active = False
        

#7.7 LOOP INFINITO

while True:
    print("Imprimindo inifinitamente ...")
    


#7.8 Lanchonete
sandwich_orders = ["Hendriks", "Chuc Barry", "Pistols", "U2"]
finished_sandwiches = []

while sandwich_orders:
    current_order = []
    current_order = sandwich_orders.pop()
    print(f"O seu sanduiche: {current_order} está pronto!")
    finished_sandwiches.append(current_order)

for sandwich in finished_sandwiches:
    print(sandwich.title())
 

   
#7.9 Sem Pastrami
sandwich_orders = ["Pastrami", "Hendriks", "Pastrami", "Chuck Barry", "Pistols", "U2", "Pastrami"]
finished_sandwiches = []

print("\nAcabou o Pastrami! Não serviremos esse sanduíche hoje.\n")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
    
while sandwich_orders:
    current_order = []
    current_order = sandwich_orders.pop()
    print(f"\tO seu sanduíche: {current_order} está pronto!")
    finished_sandwiches.append(current_order)

print("\nLista de pedidos prontos: \n")
for sandwich in finished_sandwiches:
    print("\t", sandwich.title())

'''

#7.10 Férias tão sonhadas
responses = {}
polling_active = True

while polling_active:
    name = input("Qual é o teu nome? ")
    responses[name] = input("Se pudesse visitar qualquer lugar do mundo para onde iria? ")
    
    repeat = input("Gostaria de continuar com a pesquisa (yes/ no)? ")
    if repeat == 'no':
        polling_active = False

print("\n--- Resultado da pesquisa ---\n")
for name, response in responses.items():
    print(f"{name.title()} quer ir ao seguinte local: {response.title()}")