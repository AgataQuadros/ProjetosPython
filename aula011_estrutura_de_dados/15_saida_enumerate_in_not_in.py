import os


os.system('cls')

print('-' * 70)
print('SAÍDA COM IN E NOT IN')
print('=' * 70)

# exemplo com in
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

if (3 in lista_numeros):
    print(lista_numeros)
    posicao = lista_numeros.index(3)
    print(f'O número 3 esta na posição {posicao}')
else:
    print('O elemento não costa na listagem')

print()

# exemplo com not in
lista_nomes = ['John', 'Jane', 'Carol']

if ('Maria' not in lista_nomes):
    # antes
    print(lista_nomes)

    # não esta na lista, acrescentar
    lista_nomes.append('Maria')

    print('\nO nome Maria foi acrescentado')
    print(lista_nomes)

print('-' * 70)
print('Fim do programa!')
print('-' * 70)