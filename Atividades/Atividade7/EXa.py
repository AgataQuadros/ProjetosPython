# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Faça um programa que leia um 
# número indeterminado de notas 
# (pressione ‘s’ ou ‘0’ para sair).



# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
print('-' * 20)

# Declaração
lista_aux = []
notas = []
soma = 0
media = 0

# entrada
for i in notas:
    if 's' or 0 != notas:
        notas.append(int(input(f' Entre com a nota do {i}° aluno: ')))
    else:
        print('Fim da datação de notas')