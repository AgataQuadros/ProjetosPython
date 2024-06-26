import os


os.system('cls')


meu_dicionario = {}

while True:
    print('-' * 70)
    print('\nMenu de opções:')
    print('1. Adicionar uma par chave/valor')
    print('2. Mostrar chave do dicionario')
    print('3. Mostrar valores do dicionário')
    print('4. Mostrar itens do dicionário')
    print('5. Sair')
    print('-' * 70)
    
    opcao = input('escolha entre as opções: ')

    if opcao == '1':
        # Adicionar um novo par-chave do usuario
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}:{valor} adicionados')
    
    elif opcao == '2':
        # Exibe o dicionario atual
        print('Dicionário atual: ', meu_dicionario)

    elif opcao == '3':
        # Mostrar o tamanho do dicionario usando len
        tamanho = len(meu_dicionario)
        print(f'O dicionário tem {tamanho} elementos')

    elif opcao == '4':
        # Cria uma copia do dicionario usando copy() e exibe a copia
        copia_dicionario = meu_dicionario.copy()
        print('Copia do dicionario: ', copia_dicionario)

    elif opcao == '5':
        break