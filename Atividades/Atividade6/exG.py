# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Ler uma lista com 10 números, 
# depois apresente o maior e o menor 
# número da lista

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO G')
print('-' * 20)

# Entrada
entrada = []
for i in range(1,11):
    entrada.append(int(input(f' Entre com o {i}º número: ')))

# Processamento

entrada.sort()
print(f'Lista ordenada em ordem ascendente: {entrada}')

print(f'O menor numero da sua lista é: {entrada[0]}')
print(f'O maior numero da sua lista é: {entrada[9]}')