# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa que imprima os valores no 
# intervalo definidos pelo usuário. 
# Defina 3 números que deverão ser ignorados
# , ou seja, que não serão impressos na tela.

# ENVIAR

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO H')
print('-' * 20)

# etrada
inicio = int(input('Entre com o inicio do intervalo: '))
fim = int(input('Entre com o final do intervalo: '))
intervalo = []

# Peocessamento
for c in range((inicio),(fim)):
    if c == 3:
        continue
    elif c == 5:
        continue
    elif c == 12:
        continue
    else:
        intervalo += [c]

# Saida
print('')
print('-' * 20)
print(intervalo)
print('-' * 20)
print('=' * 50)