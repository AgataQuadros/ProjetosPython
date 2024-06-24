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
while True:
    #condicional para verificar a presensa
    # de um numero especifico
    valor = int(input('verificar se o número esta na tupla'))

    if valor in tupla:
        print(f'o número {valor} esta na tupla')
        # contar quantas vezes o numero aparece
        contagem = tupla.count(valor)
        print(f'o número {valor} aparece {contagem} de vez(es)')
        # encontra o indice da 1ª ocorrencia
        indice = tupla.index(valor)
        print(f'a 1ª ocorencia de {valor} esta no índice {indice}')
    else:
        print(f'o número {valor} não esta na tupla')
    #pergunta ao usuario se deseja realizar 
    # outra operação ou sair
    continuar = input('Deseja continuar? (s/n):').lower()
    if continuar != 's':
        print('encerrando programa. Até mais!')
        break

print('-' * 70)
print('Fim do programa')
print('-' * 70)