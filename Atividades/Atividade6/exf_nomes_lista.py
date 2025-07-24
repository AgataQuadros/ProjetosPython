# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Faça um programa que 
# leia 5 nomes, depois imprima estes 
# nomes com seus respectivos índices.


# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO F')
print('-' * 20)


# Entrada
lista_nomes = ['Brendon', 'Arthur', 'Isis', 'Bia', 'Sebastião']

# Processamento
for indice, nomes in enumerate(lista_nomes):
    print(f'Nome: {nomes} = Indice: {indice}')
