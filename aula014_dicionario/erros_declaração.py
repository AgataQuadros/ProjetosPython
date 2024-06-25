import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: DICIONÁRIOS')
print('=' * 70)

# indices iguais: só exibira 1 item
dicionario1 = {'nome' : 'John', 'nome' : 'Jane'}

# Posso ter uma tupla como índice e uma lista como valor
dicionario2 = {(1,2) : [1,2]}

# Mas não posso ter uma lista como indice e uma tupla como valor

dicionario3 = {[1,2] : (1,2)}

# Saida
print('-' * 80)
print(dicionario1)
print(dicionario2)

print()