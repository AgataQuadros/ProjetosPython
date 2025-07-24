import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: LIST COMPREHENSIONS [ ]')
print('=' * 70)

lista_numeros = [1, 2, 3, 4, 5]

# triplicando os valores
lista_nova_triplicada = []

for item in lista_numeros:
    lista_nova_triplicada.append(item * 3)

print('Triplicar os valores: forma normal')
print(f'Lista triplicada: {lista_nova_triplicada}')

# list comprehension
lista_nova_triplicada2 = [item * 3 for item in lista_nova_triplicada]
print('Triplicar os valores: Lit comprehension')
print(f'Lista triplicada: {lista_nova_triplicada2}\n')