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

# Solicita ao usuario a escolher se copia a lista
escolha = input('Deseja limpar a lista? (s/n): ').strip().lower()

# reverte a lista caso for s
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa: {numeros}')
else:
    print('A lista não foi limpa.')
    
# exibe a lista base
print(f'Lista base fornecida: {entrada}')
