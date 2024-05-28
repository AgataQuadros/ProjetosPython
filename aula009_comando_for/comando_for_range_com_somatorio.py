import os


os.system('cls')

print('-' * 50)
print('ESTRUTURA DE CONTROLE SOMATÓRIO')
print('=' * 50)

print()

soma = 0

for var_interadora in range(0, 4) :
    numero = int(input(f'Digite o {var_interadora + 1}° numero: '))
    # Cáuculo
    soma += numero # mesma coisa: soma = soma + numero

print('-' * 50)
print(f'A soma dos número é: {soma}')
print('-' * 50)
print('')