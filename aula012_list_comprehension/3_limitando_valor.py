import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: LIST COMPREHENSIONS [ ]')
print('=' * 70)

lista_precos = [100, 200, 300, 400, 500, 600]

lista_com_juros = []

for valor in lista_precos:
    if valor < 300:
        lista_com_juros.append(valor * .10)

print('Aplicar 10% de juros: forma normal')
print(f'Lista triplicada: {lista_com_juros}')
print()

# list comprehensions
lista_com_juros2 = [valor +(valor * .10) 
                    for valor in lista_precos if valor < 300]
print('Aplicar 10% de juros: List comprehension')
print(f'Lista triplicada: {lista_com_juros2}')