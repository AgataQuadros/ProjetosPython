# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa que receba um número inteiro e mostre na tela:
# • A quantidade de unidades, a quantidade de dezenas,
#  a quantidade de centenas e a quantidade de milhares.

# ENVIAR

# Biblioteca
import os
import math


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO G')
print('-' * 20)

#Entrada
numero = int(input('Entre com um numero inteiro: '))

#processamento
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Saida
print('')
print('-' * 20)
print(f'O seu numero {numero} tem:')
print(f'{unidade} unidades')
print(f'{dezena} dezenas')
print(f'{centena} centena')
print(f'{milhar} unidades de milhar')
print('-' * 20)
print('fim do exercício :D')
print('=' * 50)