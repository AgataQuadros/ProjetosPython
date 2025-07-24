# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
print('-' * 20)

# Entrada
valor = int(input('digite um numero inteiro: '))
resposta = ''

# Condicional
if valor % 2 == 0:
      valor = int(valor)
      resposta = f'o valor {valor} é um numero par'
else:
      resposta = f'o valor {valor} é um numero impar'

# Saída
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('fim do exercício')
print('=' * 50)