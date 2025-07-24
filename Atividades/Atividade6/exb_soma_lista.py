# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Crie uma lista com 
# 5 números inteiros. 
# Depois imprima a soma desses valores.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO B')
print('-' * 20)

lista_numeros = []

# Entrada
lista = (input('Digite 5 números inteiros separando-os por espaço: '))
soma = 0

# Processamento
lista = lista.split()
lista_numeros.extend(lista)

for item in lista_numeros:
    item = int(item)
    soma += item

print(soma)