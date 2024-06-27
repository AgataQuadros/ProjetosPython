import os


os.system('cls')

# inicialização do dicionario e da lista
elementos = {} # dicionario
periodica = [] # lista

# entrada de dados
for c in range(2): # considerando a entrada de 2 elementos
    print(f'Entrada de dados {c + 1}')
    simbolo = str(input('Simbolo do elemento: '))
    nome = str(input('Nome do elemento: '))

    # adciona os dados ao dicionario
    elementos['simbolo'] = simbolo
    elementos['nome'] = nome
    # usa append() com copy para adicionar a lista 
    periodica.append(elementos.copy())

print()
print('-' * 70)
print('Elementos da tabela periódica')
print('-' * 70)
print()

# for aninhado para percorrer a lista e o dcionário
print('Detalhes dos elementos:')
for elemento in periodica: # para cada elemento na lista
    for chave, valor in elemento.items(): # para cada valor-chave do dicionario
        print(f'{chave.captalize()}: {valor}') # imprime a chave e o valor de maneira legivel
    print('-' * 70)# linha separadora entre elementos