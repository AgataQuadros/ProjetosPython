# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo:Faça um programa para criar um dicionário com nomes de frutas.
# Em seguida verifique se tem abacaxi nos valores.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO J')
print('-' * 20)

# Declarando
frutas = {}

# Atribuindo
frutas['a'] = 'Melancia'
frutas['b'] = 'Pitaia'
frutas['c'] = 'Carambola'
frutas['d'] = 'Abacaxi'
frutas['e'] = 'Limão'
frutas['f'] = 'Manga'
frutas['g'] = 'Romã'

# Processamento
if 'Abacaxi' in frutas:
    print()
    print('Tem Abacaxi no dicionario!!')
else:
    print()
    print('não tem Abacaxi no dicionario :(')


# Saida
print()
print('Lista das frutas')
print(frutas)
print()
print('-' * 20)
print('Fim do programa')
print('=' * 50)