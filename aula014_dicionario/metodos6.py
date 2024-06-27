import os





agenda = {
    'Jojo': '99196-3030',
    'Dio': '99196-5050',
    'Jolyne': '99196-6060',
    'Lisa Lisa': '99196-7070',
    'Speedwagon': '99196-8080',
    'Zeppeli': '99196-9090',
    'Suzie Q': '99196-0000'
}

while True:
    os.system('cls')

    print('-' * 70)
    print('\nAgenda de contatos:')
    for nome, telefone in agenda.itens():
        print(f'{nome}:{telefone}')
    print('=' * 70)

    if 'Jojo' in agenda:
        print('Primeiro teste: verificando se jojo está no Dicionário')
        print('VERDADEIRO! Jojo esta no dicionário')
    else:
        print('FALSO! Jojo não esta no dicionário')

    print()

    if 'John' not in agenda:
        print('Segundo teste: verificando se John não está no Dicionário')
        print('VERDADEIRO! Jojo não esta no dicionário')
    else:
        print('FALSO! John esta no dicionário')


    print('-' * 70)
    print('\nMenu de opções:')
    print('1. Adicionar um contato')
    print('2. Remover um contato')
    print('3. Verificar contato específico')
    print('4. Mostrar agenda')
    print('5. Sair')
    print('-' * 70)

    opcao = input('escolha entre as opções: ')

    if opcao == '1':
        # Adiciona um contato
        nome = input('Digite o nome do contato:')
        telefone = input('Digite o telefone do contato:')
        agenda[nome] = telefone
        print(f'Contato {nome}:{telefone} adicionado')

    elif opcao == '2':
        # Remover contato
            nome = input('Digite o nome do contato para remover: ')
            telefone = input('digite o telefone do contato: ')
            
            if nome in agenda:
                print(f'Contato {nome} removido. ')
            else:
                print(f'Contato {nome} não esta na agenda')
    elif opcao == '3':
        # verificar contato específico
        nome = input('Digite o nome do contato que deseja verificar: ')
        if nome in agenda:
                print(f'Contato encontrado - {nome}:{agenda[nome]}')
        else:
                print(f'Contato {nome} não esta na agenda')
    elif opcao == '4':
        # Mostrar agenda atual
        print('\n Agenda de contatos')
        print(agenda)

    elif opcao == '5':
        print('Saindo do programa...')
        break
    else:
        # mensagem de operação invalida
        print('Opção invalida. Tente novamente')