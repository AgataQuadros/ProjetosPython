import os


os.system('cls')


meu_dicionario = {}

while True:
    print('-' * 70)
    print('\nMenu de opções:')
    print('1. Adicionar uma par chave/valor')
    print('2. Remover itens usando pop()')
    print('3. Remover o ultimo item usando popitem()')
    print('4. Mostrar dicionário atual')
    print('5. Sair')
    print('-' * 70)
    
    opcao = input('escolha entre as opções: ')

    if opcao == '1':
        # Adiciona um novo par-chave ao dicionario
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}:{valor} adicionados')
    
    elif opcao == '2':
        # remover um item especifico usando pop()
        if meu_dicionario:
            chave = input('Digite a chave que deseja remover')
            valor_removido = meu_dicionario.pop(chave, 'Chave não encontrada')
            print(f'Item removido: {chave}: {valor_removido}')
        else:
            print('O dicionário esta vazio. Adicione itens primeiro')

    elif opcao == '3':
        # Remover o ultimo item usando popitm()
        if meu_dicionario:
            chave, valor = meu_dicionario.popitem()
            print(f'Ultimo item relovido: {chave}: {valor}')
        else:
            print('O dicionário esta vazio. Adicione itens primeiro')

    elif opcao == '4':
        # Mostrar o dicionario atual
        if meu_dicionario:
            print('Dicionario atual: ', meu_dicionario)
        else:
            print('O dicionário esta vazio. Adicione itens primeiro')


    elif opcao == '5':
        print('Saindo do programa...')
        break
    else:
        # mensagem de operação invalida
        print('Opção invalida. Tente novamente')