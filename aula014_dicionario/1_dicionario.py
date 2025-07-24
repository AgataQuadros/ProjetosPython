import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: DICIONÁRIOS')
print('=' * 70)


compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# Atribuindo
compras['id'] = 1
compras['item'] = 'caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'Sherlock Holmes'
pessoas['endereço'] = 'Baker Street'
pessoas['numero'] = '221B'
pessoas['cidade'] = 'Londres'
pessoas['pais'] = 'inglaterra'

cores['red'] = 'Vermelho'
cores['green'] = 'Verde'
cores['blue'] = 'Azul'

elementos['Pb'] = 'Chumbo'
elementos['Au'] = 'Ouro'
elementos['N'] = 'Nitrogênio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

print(f'Minhas compras: {compras}')
print(f'Detetives: {pessoas}')
print(f'Cor RGB: {cores}')
print(f'Tabela periódica: {elementos}')
print(f'Listagem de números: {numeros}')
print()
print('-' * 100)