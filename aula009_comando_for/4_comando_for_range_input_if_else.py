import os


os.system('cls')

print('-' * 50)
print('ESTRUTURA DE CONTRLE COM INPUT E IF')
print('=' * 50)

print('')

soma = 0

for var_iteradora in range(0, 4) :
    numero = int(input(f'{var_iteradora+ 1}° número: '))

    if (numero % 2 == 0):
        print(f'o número {numero} é par')
    else:
        print(f'O número {numero} é impar')

print('-' * 50)
print('')