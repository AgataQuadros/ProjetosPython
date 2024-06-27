import os


os.system('cls')


meu_dicionario = {}

while True:
    print('-' * 70)
    print('\nMenu de opções:')
    print('1. Adicionar uma par chave/valor')
    print('2. Definir valor padrão para uma chave usando stdefault()')
    print('3. Atualizar o dicionário usando update()')
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
        # Define valor padrão para uma chave usando setdefault()

            chave = input('Digite a chave para definir um valor padrão: ')
            valor_padrao = input('digite o valor padrão: ')
            valor_existente = meu_dicionario.setdefault(chave, valor_padrao)
            print(f'Valor para a chave: {chave}: {valor_existente}')

    elif opcao == '3':
        # Atualizar o dicionario usando update()
        novos_pares = input('Digite os novos pares: ')
        novos_pares_lista = novos_pares.split(',')
        novos_dados = {}
        for par in novos_pares_lista:
            chave, valor = par.split()
            novos_dados[chave] = valor
        meu_dicionario.update(novos_dados)
        print('Dicionário atual:', meu_dicionario)

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