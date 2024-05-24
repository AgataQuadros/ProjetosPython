# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa que receba o nome completo de uma pessoa e,
# em seguida, mostre o primeiro e o último nome.

# ENVIAR

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO I')
print('-' * 20)

# entrada
nome_completo = str(input('Entre com o seu nome completo: '))

nome_qubrado = nome_completo.split()
prime_nome = nome_qubrado[0]
ulti_nome = nome_qubrado[-1]
prime_ulti = prime_nome + ' ' + ulti_nome

#saida
print('')
print('-' * 20)
print(f'nome completo: {nome_completo}')
print(f'nome quebrado: {nome_qubrado}')
print(f'Ola! {prime_ulti}')
print('-' * 20)
print('fim do exercício :D')
print('=' * 50)