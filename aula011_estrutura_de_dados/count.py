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

# solicita ao usuario para inserir o número que deseja contar na lista
numero_para_contar = int(input('Digite o número que deseja contar: '))

# Conta o número de vezes que o número fornecido aparece na lista
contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'O número {numero_para_contar} aparece {contagem} vezes na lista.')
else:
    print(f'O número {numero_para_contar} não aparece na lista')

# exibe a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')
