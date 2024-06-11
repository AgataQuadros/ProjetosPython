import os


os.system('cls')

#solicita ao ususario para inserir números separados por espaço
entrada = input('Digite a sequencia de numeros separando-os por espaço: ')

# Divide a string de entrada em lista de string
numero_str = entrada.split()

#converte a string em lista de inteiros
numeros = []
for num_str in numero_str:
    numeros.append(int(num_str))

# Solicita ao usuario para inserir o número que deseja encontrar na lista
busca_numero = int(input('Digite o número que deseja encontrar: '))

# Tenta encontrar o indice do número fornecido
if busca_numero in numeros:
    indice = numeros.index(busca_numero+1)
    print(f'O número {busca_numero} entá no índice {indice}.')
else:
    print(f'O número {busca_numero} não foi encontrado na lista')
    
# Exibe a lista basestring
print(f'Lista fornecida: {numeros}')
