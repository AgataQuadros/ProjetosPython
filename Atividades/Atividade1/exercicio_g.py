# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 12/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO G')
print('-' * 20)

# Entrada
metros = float(input('Digite o metro: '))

# Processamento
centimetros = metros * 100
milimetros = metros * 1000

# Saida
print('')
print('-' * 20)
print(f'A converção dos metros {metros} para centímetros é {centimetros}')
print(f'A converção dos metros {metros} para milímetros é {milimetros}')
print('-' * 20)
print('')
print('=' * 50)