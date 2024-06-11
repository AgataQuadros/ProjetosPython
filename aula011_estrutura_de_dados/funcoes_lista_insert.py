import os


os.system('cls')

# Lista original
lista = [1, 2, 3, 4]

# Pedido ao usuário para fornecer a
# posição e o elemento
posicao = int(input('Posição onde deseja inserir o elemento: '))
elemento = input('Elemento a ser inserido:')

# Verifição da posição fornecida pelo usuario
if posicao >= 0 and posicao <= len(lista):
    # Inserindo o elemento na lista na posição especificada pelo usuário
    lista.insert(posicao, elemento)
    print('Lista após a inscrição:', lista)
else:
    print(f'Posição fora do intervalo 0, {len(lista)}')