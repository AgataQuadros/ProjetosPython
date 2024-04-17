# import
# Biblioteca para interagir o SO
import os
# Biblioteca para pegar data e hora do sistema
import datetime


# limparo terminal
os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS EM PYTHON')
print('=' * 70)

# entrada
nome = input('Entre comseu nome: ')
peso = input('Entre com seu peso: ')
altura = input ('Entre com sua altura:')

# entrada com Casting 
nascimento = int(input('Data de nascimento: '))
cep = int(input('Entre com seu CEP'))
bairro = str(input('Entre com seu bairro: '))
rua = str(input('Entre com sua rua:'))
numero = int(input('Entree com o número: '))

# Processamento: Pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# saida
print('-' * 70)
print('SAIDA DE DADOS')
print('=' * 70)
print('Nome: ', nome)
print('Data de nascimento: ', nascimento)
print('Peso: ', peso)
print('Altura: ', altura)

# saida interpolar
print(f'{nome}, você tem {idade} anos!')
print(f'CEP: {cep}')
print(f'Bairro: {bairro}')
print(f'Rua: {rua}')
print(f'Numero: {numero}')
print('=' * 70)
print('-' * 70)
print('')