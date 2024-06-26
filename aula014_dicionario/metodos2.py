import os


os.system('cls')


meu_dicionario = None

# Loop principal
while True:
    print('-' * 70)
    # Exibição do menu de opções
    print('\nMenu de opções:')
    
    print('1. Cria dicionário com fromkeys()')
    print('2. Buscar valor de uma chave com get()')
    print('3. Sair')
    print('-' * 70)

    opcao = input('escolha entre as opções: ')

    if opcao == '1':
        # Criação de um dicionario usando fromkey
        chaves = input('Digite as chaves separadas por ",": ').split(',')
        valor_padrao = input('Digite o valor padrão para as chaves: ')
        meu_dicionario = dict.fromkeys(chaves, valor_padrao)
        print('Dicionário criado: ', meu_dicionario)
    
    elif opcao == '2':
        # Verificar se o dicionario foi criado
        if meu_dicionario is not None:
            chave = input('Digite a chave que deseja buscar: ')
            valor = meu_dicionario.get(chave, 'Chave não encontrada')
            print(f'Valor para a chave "{chave}" : {valor}')
        else:
            print('Erro! Crie um dicionário')
    
    elif opcao == '3':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente')