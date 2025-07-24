import os


os.system('cls')

# Indicializa uma lista de Exemplo
lista_numeros = [10,20,30,40,50,60,70,80,90,100]

# Solicita ao usuário para inserir um indice para remove-lo
indice = int(input('digite o índice do elemento a ser removido (0-9): '))

# verifica se o indice esta dentro do intervalo da lista
if 0<= indice < len(lista_numeros):
    # remove o elemento e o exibe
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido: {elemento_removido}')
else:
    print('indice invalido!')

# Lista resultante
print('lista após remoção: ', lista_numeros)