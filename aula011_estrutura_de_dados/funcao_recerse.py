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
# exibe a lista fornecida para referencia
print('lista fornecida:', numeros)

# Solicita ao usuario a escolher se reverte a lista
escolha = input('Deseja inverter a ordem da lista? (s/n): ').strip().lower()

# reverte a lista caso for s
if escolha == 's':
    numeros.reverse()
    print('Lista invertida:', numeros)
else:
    print('A lista não foi invertida.')
