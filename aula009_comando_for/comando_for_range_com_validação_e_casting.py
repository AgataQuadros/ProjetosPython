import os


os.system('cls')

print('-' * 50)
print('ESTRUTURA DE CONTROLE VALIDAÇÃO E CASTING')
print('=' * 50)

soma = 0

for c in range(0, 5) :
    numero = input('Digite um numero de 0-5: ')

    #validação
    if (not(numero.isnumeric())):
        print(f'"{numero}" Entrada inválida!')
        print()
    else:
        # Casting da variável, ou seja, vai virar um inteiro
        numero = int(numero)

        #validando o intervalo pedido
        if (numero >=0 and numero <= 5) :
            print(f'O número {numero} esta dentro do intervalo!')
            print()
        else:
            print(f'"{numero}" Entrada inválida!')
            print()

print('-' * 50)
print()