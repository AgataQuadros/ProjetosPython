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
notas = []
soma = 0
media = 0

# Entrada
for i in range(1,5):
    notas.append(int(input(f' Entre com a nota do {i}º aluno: ')))

# Processamento
for nota in notas:
    soma += nota

media = soma / 4

print(f'A média dos alunos: {media}')