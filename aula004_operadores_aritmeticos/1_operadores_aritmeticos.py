# import
import os

# Limpar terminal 
os.system('cls')

print('-' * 70)
print('OPERADORES ARITMÉTICOS')
print('-' * 70)

# Entrada de dados
print('--------- SOMA')
print('-' * 70)
parcela_1 = float(input('Entre com a 1ª parcela: '))
parcela_2 = float(input('Entre com a 2ª parcela: '))

print()
print('---------- SUBITRAÇÃO')
print('-' * 70)
minuendo = float(input('Encontre o minunendo: '))
subtraendo = float(input('Encontre o subtraendo: '))

print()
print('---------- PRODUTO')
print('-' * 70)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print()
print('--------- DIVISÃO')
print('-' * 70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

print()
print('--------- RAIZ QUADRADA')
print('-' * 70)
numero_raiz_quadrada = float(input('Entre com o númmero para caculo: '))


print()
print('--------- RAIZ CUBICA')
print('-' * 70)
numero_raiz_cubica = float(input('Entre com o númmero para caculo: '))

# Processamento
soma = parcela_1 + parcela_2
diferença = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = numero_raiz_quadrada ** (1/2)
raiz_cubica = numero_raiz_cubica ** (1/3)

# Saida
print('=' * 70)
print('RESULTADOS')
print('-' * 70)
print(F'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtação de {minuendo} - {subtraendo} é: {diferença}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} / {divisor} é: {produto}')
print(f'A raiz quadrada de {numero_raiz_quadrada} é: {raiz_quadrada}')
print(f'A raiz cúbica de {numero_raiz_cubica} é: {raiz_cubica}')
print('=' * 70)
