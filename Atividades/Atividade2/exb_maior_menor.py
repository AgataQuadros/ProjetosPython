# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO B')
print('-' * 20)

# Entrada
a = int(input('digite o primeiro número: '))
b = int(input('digite o segundo número: '))
c = int(input('digite o terceiro número: '))
valor = a,b,c
resposta = ''

# Processamento
if a > b and a > b :
    resposta = f'o maior número é {a}'
elif b > c and b > a:
    resposta = f'o maior número é {b}'
elif a == b and b == c:
    resposta = f'todos os números são iguais'
else:
    resposta = f'o maior número é {c}'

# Saída
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('fim do exercício')
print('=' * 50)