# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Faça um programa que preencha 
# uma lista com as notas de 4 alunos, 
# depois imprima a média.


# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)

# Funções
lista_aux = []

# Entrada
nota_1 = input('Entre com a nota do 1° aluno:')
nota_2 = input('Entre com a nota do 2° aluno:')
nota_3 = input('Entre com a nota do 3° aluno:')
nota_4 = input('Entre com a nota do 4° aluno:')

notas = nota_1,nota_2,nota_3,nota_4
lista_aux = notas.split(notas)
