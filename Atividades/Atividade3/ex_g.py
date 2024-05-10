# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa que peça os valores de a, b e c de uma equação do 2º grau.
# Calcule as raízes da equação do 2º grau seguindo a fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a)

# ENVIAR

# Biblioteca
import os
import math

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO G')
print('-' * 20)

# Entrada
a = int(input('Entre com o valor de A: '))
b = int(input('Entre com o valor de B: '))
c = int(input('Entre com o valor de C: '))
resposta = ''

# Processamento
discriminante = b**2 - 4*a*c
rd = math.sqrt(discriminante) # raiz descriminante
r1 = (-b + rd) / (2*a) # raiz 1
r2 = (-b - rd) / (2*a) # raiz 2

if rd > 0 :
   resposta = (f'O resultado da sua equação é: '
   f'raiz positiva = {r1} raiz negativa = {r2}')
else:
   resposta = f'Desculpa mas a sua equação é incalculavel'

# Saída
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('=' * 50)