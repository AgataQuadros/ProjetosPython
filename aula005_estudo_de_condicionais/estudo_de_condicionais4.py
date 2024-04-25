# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Sebastião Marcos
# Data 12/04/2024
#estudo de condicionais: PT4
# operadores lógicos

# Importando da Biblioteca
import os


# Limpando o terminal
os.system('cls')

# Declaração
a = 10
b = 5
c = 'John'

print('-' * 70)
print('Condicional: Operadores Lógicos')
print('-' * 70)

# E (and) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('.' * 70)

# E (and) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('.' * 70)

# OU (or) VERDADEIRO
print('OU (or) VERDADEIRO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('.' * 70)

# OU (or) FALSO
print('OU (or) FALSO')
if (a < 5 or c == 'Jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')
print('-' * 70)
print()