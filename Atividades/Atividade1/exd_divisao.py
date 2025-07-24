# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 12/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)

# Entrada
dividendo = (float(input('Entre com o divendendo: ')))
divisor = (float(input('Entre com o divisor: ')))

# Processamento
resultado = dividendo / divisor

# Saída
print('')
print('-' * 20)
print(f'O resultado da divisão entre {dividendo} / {divisor} é {resultado: .4f}')
print('-' * 20)
print('')
print('=' * 50)