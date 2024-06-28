# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo:Faça um programa para criar um dicionário com 4 elementos.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
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

# Saida
if entrada == '':
    print(usuario)
else:
    print('Saindo do painel de entrada.')

print('-' * 20)
print('Fim do programa')
print('=' * 50)