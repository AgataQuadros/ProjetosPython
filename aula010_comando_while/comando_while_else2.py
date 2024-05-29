import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE WHILE ELSE BREAK')
print('=' * 70)

print()

while (True):
    #lower() garante o tratamento para entrada de 's' ou 'S'
    nome = str(input('Digite o seu nome (ou digite "s" para sair): '))

    if (nome != 's'):
        print('Continue digitandp...')
    else:
        print('-' * 70)
        print('Você digitou "s" para sair!')

        # intrrompe laço
        break


print('-' * 70)
print()