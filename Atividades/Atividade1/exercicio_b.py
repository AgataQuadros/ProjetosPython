# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 12/04/2024

# Biblioteca
import os
import datetime

# Limpar o terminal
os.system('cls')

print('=' * 50)
print('EXERCICIO B')
print('-' * 20)

# Entrada

nascimento = int(input('Digite em qual ano você nasceu: '))

# Processamento
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# Saida
print('-' * 20)
print('')
print(f'Ora, se você nasceu no ano {nascimento} então você tem {idade} anos!')
print('')
print('=' * 50)