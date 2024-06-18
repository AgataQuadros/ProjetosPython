# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Faça um programa que leia as vogais,
# depois mostre-as em ordem inversa.


# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO E')
print('-' * 20)

# Entrada
vogais = ['a', 'e', 'i', 'o', 'u']


# Processamento
vogais_copia = vogais.copy()
vogais_copia.reverse()

# Saida
print(f'Ordem inversa das vogais: {vogais_copia}')