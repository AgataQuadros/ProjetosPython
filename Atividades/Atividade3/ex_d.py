# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa que receba um ângulo qualquer. 
# Em seguida, calcule o seno, cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.

# ENVIAR

# Biblioteca
import os
import math

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)

# Entrada
angulo = float(input('Entre com o seu angulo: '))

# Processamento

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Saída
print('')
print('-' * 20)
print(f'Aqui estão o seu seno {seno}, o seu'
      f'cosseno {cosseno} e a sua tangente {tangente}')
print('-' * 20)
print('=' * 50)