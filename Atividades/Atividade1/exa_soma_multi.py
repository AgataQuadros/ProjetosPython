# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 12/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
print('-' * 20)

# Entrada
valor1 = float(input('Digite o 1ª elemento: '))
valor2 = float(input('Digite o 2ª elemento: '))
valor3 = float(input('Digite o 3ª elemento: '))

# Processamento
soma = valor1 + valor2 + valor3
multiplicacao = valor1 * valor2 * valor3

# Saída
print('')
print('-' * 20)
print('RESULTADOS')
print('-' * 20)
print(f'A sua soma dos valores {valor1} + {valor2} + {valor3} resulta em {soma}')
print(f'A sua multiplicação dos valores {valor1} x {valor2} x {valor3} result em {multiplicacao}')
print('=' * 50)