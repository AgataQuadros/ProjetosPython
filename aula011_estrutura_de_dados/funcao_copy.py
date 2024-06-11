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
escolha = input('Deseja criar uma copia da lista? (s/n): ').strip().lower()

# reverte a lista caso for s
if escolha == 's':
    lista_copiada = numeros.copy()
    print(f'Copia da lista: {lista_copiada}')
else:
    print('A lista não foi copiada.')
    
# exibe a lista base
print(f'Lista base fornecida: {numeros}')
