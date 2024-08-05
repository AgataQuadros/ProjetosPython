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

def cadastrar(**aluno):
    alunos = aluno
    cadastro.append(alunos.copy())

while True:
    print('°.______CADASTO DE ALUNOS______.°')
    menu = input('1 - CADASTRAR ALUNO | 2 - SAIR: ')
    
    if '1' in menu:
        nome = input('Insira o nome do aluno: ')
        matricula = input('Insira a matricula: ')
        nascimento = input('Insira a data de nascimento: ')
        cadastrar(nome=nome, matricula=matricula,
                      nascimento=nascimento)

    elif '2' in menu:
        print('Encerrando...')
        break

    else:
        print('opção invalida!!')
        break