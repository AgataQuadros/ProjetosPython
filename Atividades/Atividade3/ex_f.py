# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024
# Objetivo: Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’


# ENVIAR

# Biblioteca
import os
import random

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO F')
print('-' * 20)

# Entrada
numero = random.randint(1,10)
n_user = int(input('Tente adivinhar o numero que eu estou pensando: '))
resposta = ''

# Processamento
if n_user == numero:
    resposta = f'Eba!! você acertou o numero realmente era {numero}!!'
else:
    resposta = f'Ah não era esse numero que eu estava pensando, tenta de novo! (o numero era {numero} mas não conta pra ninguem)'

# Saída
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('Mais Um, ' * 4)
print('=' * 50)