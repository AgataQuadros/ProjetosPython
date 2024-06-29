# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo:Faça um programa que peça continuamente 
# o nome e a idade de uma pessoa.
# Caso o usuário digite a idade 999, o programa será finalizado 
# e executará uma impressão com os nomes cadastrados.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO K')
print('-' * 20)

# Declarando
usuario = {}

# Processamento
while True:
    print()
    nome = str(input('Entre com o nome: '))
    idade = int(input('Entre com a idade: '))
    usuario[nome] = idade

    if idade == 999:
        print('Idade invalida.')
        valor_removido = usuario.popitem()
        break


# Saida
print()
print('Informações inseridas:')
print(usuario)
print()
print('-' * 20)
print('Fim do programa')
print('=' * 50)