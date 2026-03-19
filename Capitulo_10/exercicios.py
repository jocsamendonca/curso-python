from pathlib import Path
'''

#10.1 Aprendendo Python

path = Path("Capitulo_10/learning_python.txt")
contents = path.read_text()
# print(contents)

# lines = contents.splitlines()
learning_string = ''
for line in contents.splitlines():
    learning_string += f"{line}. "

print(learning_string)

# print(contents_list)
for content in contents_list:
    print(content)

#10.2 Aprendendo C

for line in lines:
    c = line.replace('Python', 'C')
    print(c)

# 10.04Convidados

name = input("Informe seu nome: ")

path = Path('Capitulo_10/guest.txt')
path.write_text(name)


# 10.5 Livro de convidados
convidados = ''
while True:
    name = input("Informe o nome ou 'sair' para finalizar: ")
    if name == 'sair':
        break
    convidados += f"\t- {name}\n"
    
# convidados = ''.join(convidados)       
path = Path('Capitulo_10/guest_book.txt')
path.write_text(convidados)

#10.6 Operação de soma
#10.7 Calculadora de soma
print("\nGive me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add by literal!")
    else:
        print(answer)

#10.8

# Criando o arquivo cats.txt e adicionando nomes de gatos
with open('cats.txt', 'w') as f:
    f.write('Miau\n')
    f.write('Bolinha\n')
    f.write('Peludo\n')

# Criando o arquivo dogs.txt e adicionando nomes de cachorros
with open('dogs.txt', 'w') as f:
    f.write('Rex\n')
    f.write('Toby\n')
    f.write('Max\n')

filenames = ['cats.txt', 'dogs.txt']

def ler_arquivos(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        #10.9 sem acusar erros
        pass
        # print(f"O arquivo {path} não existe!")
    else:
        print(contents)
    
for filename in filenames:
    path = Path(filename)
    ler_arquivos(path)

# 10.10 Palavras comuns
filenames = ['MobyDick.txt', 'MemoriasPosthumasdeBrazCubas.txt']

def count_word(path, word):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"O arquivo {path} não existe!")
    else:
        num_word = contents.lower().count(word)
        print(f"The file {path} has about {num_word} appers of {word}.")
    
for filename in filenames:
    path = Path(filename)
    count_word(path, 'the')
'''
# 10.11 Número favorito
