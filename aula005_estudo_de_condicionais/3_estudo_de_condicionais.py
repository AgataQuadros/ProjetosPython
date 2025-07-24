# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Sebastião Marcos
# Data 12/04/2024
#estudo de condicionais parte 2
# Objetivo: Pratica com condicionais simples aninhadas

import os


os.system('cls')


a = 10
b = 5
c = 'José'
d = 'José'

print('-' * 70)
print('Estudo de Condicional (Simples)')
print('=' * 70)

# Igualdade (==)
if a == b:
    print('-' * 70)
    print(f'{a} é igual que {b}')
    print('=' * 70)
else:
    print(f'{a} não é igual que {b}')

# diferença (!=)
if a != c:
    print('-' * 70)
    print(f'{a} é igual que {c}')
    print('=' * 70)
else:
    print(f'{a} não é igual que {c}')

# Maior que (>)
if a > b:
    print('-' * 70)
    print(f'{a} é maior que {b}')
    print('=' * 70)
else:
    print(f'{a} não é maior que {b}')

    # Menor que (<)
if a < b:
    print('-' * 70)
    print(f'{b} é menor que {a}')
    print('=' * 70)
else:
    print(f'{b} não é menor que {a}')

    # Maior Igual (>=)
if a >= b:
    print('-' * 70)
    print(f'{a} é maior ou igual que {b}')
    print('=' * 70)
else:
    print(f'{a} não é maior igual que {b}')

    # Menor Igual (<=)
if b <= a:
    print('-' * 70)
    print(f'{b} é menor ou igual que {a}')
    print('=' * 70)
else:
    print(f'{b} não é menor ou igual que {a}')

print('Fim do programa!')
print('=' * 70)
print()