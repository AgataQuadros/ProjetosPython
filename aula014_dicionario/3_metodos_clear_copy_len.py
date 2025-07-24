import os


os.system('cls')
# Crição do dicionário vazio
meu_dicionario = {}

while True:
    print('-' * 70)
    # Exibição do menu de opções
    print('\nMenu de opções:')
    
    print('1. Adicionar uma par chave/valor')
    print('2. Mostrar dicionario')
    print('3. Mostrar tamanho do dicionário')
    print('4. Copiar o dicionário')
    print('5. Limpar dicionário')
    print('6. Sair')
    print('-' * 70)
    #solicitação da escolha
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
        # Limpa o dicionario usando clear()
        meu_dicionario.clear()
        print('Dicionário limpo.')

    elif opcao == '6':
        # Sai do programa
        print('Saindo do programa...')
        break
    
    else:
        # Mensagem de opção inválida
        print('Opção inválida. Tente novamente')