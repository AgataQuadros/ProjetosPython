# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra
#  'o' aparece e em que posição ela aparece pela primeira e última vez

# ENVIAR

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO H')
print('-' * 20)

#entrada
nome = str(input('Entre com o seu nome: '))
resposta = ''

#prcessamento
numeros_de_letras = nome.count(O)

resposta = (f'O seu nome contem {numeros_de_letras} letras!')


print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('fim do exercício :D')
print('=' * 50)