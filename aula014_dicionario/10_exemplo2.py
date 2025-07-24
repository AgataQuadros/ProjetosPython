import os


os.system('cls')

print('-' * 70)
print('-------------TABELA PERIÓDICA-------------')
print('-' * 70)

# inicialização do dicionario e da lista
elementos = {} # dicionario
periodica = [] # lista

while True:
    print('-' * 70)
    print('MENU DE OPÇÕES:')
    print('1. Adicionar uma elemento')
    print('2. Visializar todos os elementos')
    print('3. Atualizar um elemento')
    print('4. Remover um elemento')
    print('5. Sair')
    print('-' * 70)
    import os
    
    opcao = input('escolha entre as opções: ')

    if opcao == '1':
        # Adiciona um novo par-chave ao dicionario
        simbolo = input('Simbolo do emlemento: ')
        nome = input('Nome do elemento: ')
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())
        print('\n Elemento adicionado. Pressione Enter para continuar...')
    
    elif opcao == '2':
        print('\nElementos da tabela periódica:')
        print('-' * 70)

        for elemento in periodica:
            for chave, valor in elemento.items(): 
                print(f'{chave.captalize()}: {valor}')
            print('-' * 70)
        input('\nPressione Enter para continuar...')

    elif opcao == '3':
        # Atualizar um elemento
        simbolo = str(input('Digite o símbolo do elemento para atualizar: '))
        # iniciando a flag como false
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input(f'Digite o novo símbolo para'
                                        f'{simbolo} (ou deixe em brenco para manter o atual):'))
                novo_nome = str(input(f'Digite o novo nome para'
                                     f'{simbolo} (ou deixe em brenco para manter o atual):'))
                # atualizando o simbolo e o nome se fornecidos
                if novo_simbolo:
                   elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome
                #define flag como true quando o elemento é encontrado
                encontrado = True
                break
        if encontrado:
            input('\nElemento atualizado. Pressione Enter para continuar...')
        else:
            input('\nElemento não encontrado. Pressione Enter para continuar...')

    elif opcao == '4':
        # removendo elemento
        simbolo = str(input('Digite o simbolo do elemento para remover: '))
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                periodica.remove(elemento)
                encontrado = True
                break
        if encontrado:
                input('\nElemento removido. Pressione Enter para continuar...')
        else:
                input('\nElemento não encontrado. Pressione Enter para continuar...')

    elif opcao == '5':
        print('Saindo do programa...')
        break
    else:
        # mensagem de operação invalida
        input('Opção invalida.Pressione Enter para tentar novamente')