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

nota1 = float(input('Lançe a 1ª nota: '))
nota2 = float(input('Lançe a ª nota: '))
nota3 = float(input('Lançe a ª nota: '))
nota4 = float(input('Lançe a 4ª nota: '))

# Processamento
soma = nota1 + nota2 + nota3 + nota4
media = (nota1 + nota2 + nota3 + nota4) / 4

# Saida
print('Média')
print('')
print(f'A média dessa turma é: {media}')
print('')
print('=' * 50)