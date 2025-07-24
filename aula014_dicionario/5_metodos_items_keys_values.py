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
        # Adiciona um novo par-chave ao dicionario
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}:{valor} adicionados')
    
    elif opcao == '2':
        # mostra as chaves do dicionario
        if meu_dicionario:
            print('Chaves do dicionário:', meu_dicionario.keys())
        else:
            print('O dicionário esta vazio. Adicione itens primeiro')

    elif opcao == '3':
        # Mostrar o valor do dicionario usando values()
        if meu_dicionario:
            print('Valores do dicionário: ', meu_dicionario.values())
        else:
            print('O dicionário esta vazio. Adicione itens primeiro')

    elif opcao == '4':
        # mostra os itens(chave-valor) do dicionario usando itens()
        if meu_dicionario:
            print('Itens do dicionário: ', meu_dicionario.items())
        else:
            print('O dicionário esta vazio. Adicione itens primeiro')


    elif opcao == '5':
        print('Saindo do programa...')
        break
    else:
        # mensagem de operação invalida
        print('Opção invalida. Tente novamente')