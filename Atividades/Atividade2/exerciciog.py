# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO G')
print('-' * 20)

# Entrada
a = int(input('entre com o primeiro valor: '))
b = int(input('entre com o segundo valor: '))
c = int(input('entre com o terceiro valor: '))

# Processamento
if (a < b + c) and (b < c + a) and (c < b + a):
    resposta = f'Opa! parece que temos sim um triangulo!'


