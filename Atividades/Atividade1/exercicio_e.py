# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 12/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO E')
print('-' * 20)

# Entrada
numero = int(input('Entre com um numero inteiro: '))

# Processamento
antecessor = numero - 1
sucessor = numero + 1

# Saida
print('')
print('-' * 20)
print(f'O sucessor do numero {numero} é {sucessor}')
print(f'O antecessor do numero {numero} é {antecessor}')
print('-' * 20)
print('')
print('=' * 50)