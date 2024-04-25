# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 12/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('-' * 70)
print('Estudo de Condicional: Pt1')
print('-' * 70)

# Entrada
valor = float(input('digite o numero decimal: '))
resposta = ''

# Condicional
if valor // 2 == 0:
      resposta = f'entrada incorreta, o valor {valor} é um inteiro'
else:
      resposta = f'entrada correta, o valor {valor} é um decimal'

# Saida 
print('=' * 70)
print(resposta)
print('fim do programa!\n') # \n salta um linha