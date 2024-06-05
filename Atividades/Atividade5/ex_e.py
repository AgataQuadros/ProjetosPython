# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Faça um programa que some a quantidade de números 
# pares encontrados no intervalo entre 0 e 100.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)

# Entrada
soma = 0

# Processamento
for c in range(0, 100):
    if c % 2 ==0:
        soma += 1
        
print('----')
print(c)