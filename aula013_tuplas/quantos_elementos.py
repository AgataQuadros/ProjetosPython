import os


os.system('cls')

#solicitar a quantidade de elementos da tupla
numero_elementos = int(input('Quantos elementos na tupla:'))

# iniciando ua lista vazia para arma zenar os elementos do usuário
elementos = []

#estrupura de repetição para obter os elementos
for i in range(numero_elementos):
    while True:
        valor = input(f'Digite o valor {i+1}:')
        if valor.isdigit():
            elementos.append(int(valor))
            break
        else:
            print('Entrada invalida. Digite um número.')

# converter a lista em tupla
tupla = tuple(elementos)

print('-' * 70)
print(f'Tupla criada:{tupla}')
print('-' * 70)

#estrutura de repetição para permitir múltiplas operações
#até o usuario deseje sair



