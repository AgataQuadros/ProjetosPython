import os


os.system('cls')

nomes = ['Ágata', 'Bia', 'coly', 'Isis']

for indice, nome in enumerate(nomes):
    #cria minha tupla contendo o índice e o nome da pessoa atual
    minha_tupla = (indice, nome)
    # a variavel minha_tupla é utilizada para acessar o 
    # índice e o nome armazenados na tupla
    # mas posso acessar diretamente os elementos 'indice' e 'nome'
    print(f'o nome "{minha_tupla[1]}", psição {minha_tupla[0]}')
    print(f'o nome "{nome}", posição {indice} da lista.')
    print('-' * 70)