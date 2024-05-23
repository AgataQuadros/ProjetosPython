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
sobrenome = str(input('Entre com o seu sobrenome: '))
ultimo_nome = str(input('Entre com o seu ultimo nome, caso não tenha, de enter: '))

#prcessamento
nome_completo = nome+sobrenome+ultimo_nome
caixa_baixa = nome_completo.lower()
caracteres = ''.join(caixa_baixa)
numeros_de_letras = caracteres.count('o')
posicao1 = caracteres.find('o')
posicao2 = caracteres.rfind('o')

#Saida
print('')
print('-' * 20)
print(f'O seu nome contem {numeros_de_letras} letras "o"')
print(f'A primeira posição em que "o" apareçe em seu nome é a {posicao1} e a ultima é a {posicao2}')
print('-' * 20)
print('fim do exercício :D')
print('=' * 50)