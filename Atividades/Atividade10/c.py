# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Crie uma função que verifica se uma aluno está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados.
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO C')
print('-' * 20)


def verificar_aluno(aluno):
    alunos = {'Nome': 'Agata Quadros',
                     'Data de nascimento': '16/09/2006', 'Matricula': '1234'}
    
    if alunos['Nome'] == aluno:
        print(f'O aluno(a) {aluno} esta no dicionario')
        for k,v in alunos.items():  
            print(k,v)
    else:
        print('Aluno(a) não encontrado')



verificar_aluno('Juca')