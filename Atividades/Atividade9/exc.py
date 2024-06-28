# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo:Utilizando o exercício anterior,
# retire um elemento do dicionário.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO C')
print('-' * 20)

# Declarado
usuario = {}

# Entrada
print()
print('Procurando usuario...')
print()
entrada = input('Usuario encontrado. Aperte enter para prosseguir...')

# Atribuindo
usuario['nome'] = 'Mônica Oliveira'
usuario['titulo'] = 'Dona da rua'
usuario['endereço'] = 'Bairro do limoeiro'
usuario['numero'] = '22'

# Processamento
if entrada == '':
    print(usuario)
    adicionar = input('Deseja adicionar mais informações ao perfil? (s/n)')
    if adicionar == 's':
        for i in range(2):
            print()
            nome = str(input('Entre com o nome da informação: '))
            informacao = str(input('Entre com a informação: '))
            usuario[nome] = informacao
    
    excluir = input('Deseja excluir alguma informação do perfil? (s/n)')
    if excluir == 's':
        print()
        nome = str(input('Digite o nome da informação que deseja remover: '))
        valor_removido = usuario.pop(nome, 'Chave não encontrada')

else:
    print('Saindo do painel de entrada.')

# Saida
print()
print('Informação retirada.')
print('Perfil atualizado:')
print(usuario)
print()
print('-' * 20)
print('Fim do programa')
print('=' * 50)