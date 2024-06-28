# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo:Utilizando o exercício anterior,
# adicione mais 2 elementos ao dicionário.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO B')
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
            nome = str(input('Entre com o nome da informação: '))
            informacao = str(input('Entre com a informação: '))
            usuario[nome] = informacao
            
else:
    print('Saindo do painel de entrada.')

# Saida
print()
print('Informações adicionadas')
print('Perfil atualizado:')
print(usuario)
print()
print('-' * 20)
print('Fim do programa')
print('=' * 50)