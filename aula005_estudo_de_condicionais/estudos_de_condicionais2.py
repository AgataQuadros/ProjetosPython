# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Sebastião Marcos
# Data 12/04/2024
#estudo de condicionais parte 2
# Objetivo: Pratica com condicionais simples aninhadas

import os


# Limpando o terminal

os.system('cls')

# Declaracões
a = 10
b =5
resposta = ''

print('-' * 70)
print('Estudo de Condicional (Simples)')
print('=' * 70)

# Condicionais
if a > b:
    resposta = f'{a} é maior que {b}'
else:
    resposta = f'{a} não é maior que {b}'
# Saida
print('-' * 70)
print(resposta)

# Declarações
a = 5
b = 5

print('-' * 70)
print('Esudo de Condicional (aninhada)')
print('=' * 70)

if a > b:
    resposta = f'{a} é maior que {b}'
elif a < b:
    resposta = f'{a} é menor que {b}'
else:
    resposta = f'Os valores são iguais: {a} = {b}'
#saida
print('-' * 70)
print(resposta)
print('-' * 70)
print()