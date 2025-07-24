# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO H')
print('-' * 20)

# Entrada
a = 1
b = -6
c = 5
x1 = 5
x2 = 1
resposta = ''

# Processamento 1: Cauculos
discriminante = b**2 - 4*a*c
raiz_discriminante = discriminante ** 0.5
raiz_1 = (-b + raiz_discriminante) / (2*a)
raiz_2 = (-b - raiz_discriminante) / (2*a)

if (raiz_1 == x1) and (raiz_2 == x2):
    resposta = f'Iay todos os valores recebidos formam a resposta correta de x1= {x1} x2 = {x2}'
else:
    resposta = f'Ops, alguma das informações fornecidas esta incorreta, tente novamente mais tarde'

# Saída
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('fim do exercício')
print('=' * 50)