# Atividade 1 DdS
# Ágata Quadros Turma: 0152

# Import
# Bilioteca para interagir com OS
import os


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

# Tipos da variavel
print('a variavel nome é do tipo: ', type(nome))
print('a variavel altura é do tipo: ', type(altura))
print('a variavel mês é do tipo: ', type(mes))
print('a variavel ano é do tipo: ', type(ano))
print('a variavel dia é do tipo: ', type(dia))
print('a variavel menor de idade é do tipo: ', type(menor_de_idade))
print('=' * 50)
