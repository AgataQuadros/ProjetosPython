# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares,
# a quantidade de números pares e a quantidade de números ímpares.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
print('-' * 20)

def pegar_pi(lista_numeros):
    print(lista_numeros)
    lista_par = []
    lista_impar = []

    for parimpar in lista_numeros:
        if parimpar % 2 == 0:
            lista_par.append(parimpar)
        else:
            lista_impar.append(parimpar)
    quantidade_pares = len(lista_par)
    quantidade_impares = len(lista_impar)
    return lista_par, lista_impar, quantidade_pares, quantidade_impares



lista_numeros = [43, 87, 12, 56, 99, 24, 78, 34, 65,]
pares, impares, qtd_pares, qtd_impares = pegar_pi(lista_numeros)

print(f'Números pares: {pares}')
print(f'Números impares: {impares}')

print(f'quatidade de pares: {qtd_pares}')
print(f'quatidade de impares: {qtd_impares}')