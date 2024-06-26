# Trabalho sobre a estrutura de dados SET
# Senac MG/JF
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data: 24/06/2024

# union(set2) ou |: Retorna um novo set que é a união de dois sets.

# O programa a seguir vai te dar um exemplo de 'union de 2 sets' 
# mostrando tambem como converter lista para set.


# Biblioteca
import os

# Limpando o terminal
os.system('cls')


print('=' * 50)
print('METODO UNION OU |')
print('-' * 50)


# entrada
entrada1 = input('Entre com a 1ª lista que você desa unir separando cada elemento por ",": ')
entrada2 = input('Entre com a 2ª lista que você desa unir separando cada elemento por ",": ')

# processamento
# tranformando as entradas em listas
lista1 = entrada1.split(',')
lista2 = entrada2.split(',')
# Transformando as listas em sets
set1 = set(lista1) # o set desordena a lista
set2 = set(lista2)
# unindo as duas lista
unidas = set1.union(set2)
unidas2 = set1 | set2
# A lista não vai ficar na sequencia exata que o usuario deu na entrada por conta do set

# Saida
print('-' * 20)
print(f'As listas fornecidas foram a {lista1} e a {lista2}')
print(f'Unindo elas com " .union " você fica com: {unidas}')
print(f'Unindo elas com " | " você fica com: {unidas2}')
print('Obrigado por participar!')
print('')
print('Fim do programa')
print('=' * 50)