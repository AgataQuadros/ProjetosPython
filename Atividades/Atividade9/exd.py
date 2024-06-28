# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo:Faça um programa para criar um dicionário com 5  cores.
# Depois,  imprima as chaves e os valores deste dicionário.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)

# Declarando
cores = {}

# Atribuindo
cores['red'] = 'Vermelho'
cores['green'] = 'Verde'
cores['blue'] = 'Azul'
cores['black'] = 'Preto'
cores['white'] = 'Branco'

# Saida
print()
print(f'Cores: {cores}')
print()
print('-' * 20)
print('Fim do programa')
print('=' * 50)