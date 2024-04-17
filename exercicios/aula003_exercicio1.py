# Atividade 1 DdS
# Ágata Quadros Turma: 0152

# Import
# Bilioteca para interagir com OS
import os

# Biblioteca para pegar data e hora do sistema
import datetime


# Limpando o terminal 
os.system('cls')

print('=' * 50) # firula
print('Exercicio 1 Aula 3')
print('=' * 50) # firula


# Entrada
nome = str(input('Escreva seu nome: '))
dia = int(input('Dia: '))
mes = str(input('Mês: '))
ano = int(input('Ano: '))
altura = float(input('Escreva sua altura: '))
menor_de_idade = True

# Saida interpolada
print('-' * 30) # Firula
print(f'Nome...........: {nome}')
print(f'Nascimento...........: {dia}/{mes}/{ano}')
print(f'Atura...........: {altura}')
print('-' * 30) # Firula




