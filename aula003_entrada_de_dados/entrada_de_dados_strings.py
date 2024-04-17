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
nome = input('Gaia')
peso = input('60.0')
altura = input ('1.57')

# entrada com Casting 
nascimento = int(input('2006'))
cep = int(imput('25259-870'))
bairro = str(input('Milha poca'))
rua = str(input('Rua.Supra do Carmo'))
numero = int(input('35'))

# Processamento: Pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade + int(ano_atual) - nascimento

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