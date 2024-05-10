# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa que receba um valor e mostre sua raiz quadrada. 
# Para raízes que não são exatas, arredonde para cima ou para baixo. 
# Faça a validação para números negativos, avisando ao usuário que o resultado será um número complexo

# Biblioteca
import os
import math

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
print('-' * 20)

# Entrada
numero = input('Entre com o radicando: ')

# Processamento
raiz_quadrada = numero ** (1/2)

# Saída