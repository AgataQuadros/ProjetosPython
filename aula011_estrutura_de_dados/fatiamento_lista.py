import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS : LISTAS [ ]')
print('=' * 70)

lista_mista = ['a', 'b', 3, 'John', 'e', 500, 'g', 'h']

#fatiamentos
#1º elemento
lista_fatiada = lista_mista[0]
#todos elementos
lista_fatiada2 = lista_mista[0:]
#indice 0 a indice 6
lista_fatiada3 = lista_mista[0:6]
#0 a 6 de 2 em 2
lista_fatiada4 = lista_mista[0:6:2]
#da direita para a esquerda
lista_fatiada5 = lista_mista[::-1]

print(f'Fatianto uma lista: {lista_fatiada}\n')
print(f'Fatianto uma lista: {lista_fatiada2}\n')
print(f'Fatianto uma lista: {lista_fatiada3}\n')
print(f'Fatianto uma lista: {lista_fatiada4}\n')
print(f'Fatianto uma lista: {lista_fatiada5}')

print('-' * 70)
print('Fim do programa!')
print('-' * 70)