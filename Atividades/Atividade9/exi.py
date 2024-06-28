# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo:Faça um programa para criar um dicionário com 4 elementos.
# Depois imprima a lista completa, 
# delete o último elemento e mostre uma listagem nova.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO I')
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
    excluir = input('Deseja excluir a ultima informação do perfil? (s/n)')
    if excluir == 's':
        print()
        valor_removido = usuario.popitem()

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