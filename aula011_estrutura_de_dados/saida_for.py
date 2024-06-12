import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS : LISTAS [ ]')
print('=' * 70)

# Criando uma lista
lista_alunos = []

for c in range(0,5):
    nome = str(input('Entre com o nome do aluno: '))
    #guardando em lista
    lista_alunos.append(nome)

print()
print('Impressão dos nomes de alunos: ')

#utilizando o len() para saber a quantidade de alunos
for aluno in range(len(lista_alunos)):
    print(lista_alunos[aluno], end=' ')
    if aluno == 3:
        print()

print('-' * 70)
print('Fim do programa!')
print('-' * 70)
