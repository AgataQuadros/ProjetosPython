# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa que receba o nome completo de uma pessoa e,
# em seguida, mostre o primeiro e o último nome.

# ENVIAR

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO I')
print('-' * 20)

# entrada
nome1 = str(input('Entre com o seu primeiro nome: '))
nome2 = str(input('Entre com o seu segundo nome: '))
nome3 = str(input('Entre com o seu terceiro nome, caso não tenha, de enter: '))
resposta = ''

#processament
pri_ult = nome1 + nome3
pime_ulti = nome1 + nome2

if ' ' in nome3:
    resposta = f'Ola! {pri_ult}'
else:
    resposta = f'Ola! {pime_ulti}'


#saida
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('fim do exercício :D')
print('=' * 50)