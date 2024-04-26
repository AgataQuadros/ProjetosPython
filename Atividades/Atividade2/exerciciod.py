# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO C')
print('-' * 20)


# Entrada
salario_atual = int(input('entre com o seu salario atual: '))
salario = 1500
resposta = ''

# Processamento
aumento_5 = salario_atual + (5/100 * salario_atual)
aumento_10 = salario_atual + (10/100 * salario_atual)

if salario_atual > 0:
   if salario_atual > salario:
     resposta = f'Opa, parabens! seu salario recebeu um almento de {salario_atual} para {aumento_5}'
   else:
     resposta = f'Opa, parabens!seu salario recebeu um aumento de {salario_atual} para {aumento_10}'
else:
    resposta = 'O valor que você nos informou é menor ou igual a 0 e por isso foi invalidado'

# Saída
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('fim do exercício')
print('=' * 50)
