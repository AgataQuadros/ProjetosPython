# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Crie uma função que cadastre o nome de um aluno,
#  a matrícula e a data de nascimento.
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO B')
print('-' * 20)

cadastro = []
aluno = {}

def cadastrar():
    aluno['nome'] = input('Insira o nome do aluno: ')
    aluno['matricula'] = input('Insira o nome do matricula: ')
    aluno['nascimento'] = input('Insira o nome do data de nascimento: ')
    
    os.system('cls')
    cadastro.append(aluno.copy())

while True:
    cadastrar()
    for info in cadastro:
        print(info)
        if 'sair' in aluno:
            break