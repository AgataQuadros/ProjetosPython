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

# Solicita ao usuario para escolher a ordem de classificação
ordem= input('Digite "asc" para ordem ascendente ou "desc" para ordem descendente: ').strip().lower()

# Verifica a escolha do usúario e ordena a lista de arcordo
if ordem == 'asc':
    numeros.sort()
    print(f'Lista ordenada em ordem ascendente: {numeros}')
elif ordem == 'desc':
    numeros.sort(reverse=True)
    print(f'Lista ordenada em ordem descendente: {numeros}')
else:
    print('Opção invalida! A lista não foi ordenada.')

# Exibe a lista base
print('Lista fornecida:', entrada)
