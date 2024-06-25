# Trabalho sobre a estrutura de dados SET
# Senac MG/JF
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data: 24/06/2024

# Os alunos farão, por sorteio, um programa (1 por aluno) utilizando os 
# métodos da estrutura de dados Set . 
# Depois de prontos, todos os exemplos gerados pelos alunos farão parte da apostila 
# de linguagem de programação python do Curso de Desenvolvimento de Sistemas. 
# Atenção para colocarem uma descrição do programa, sua data de criação,
# o ano e a turma. Como temos 14 alunos, 4 trabalhos serão feitos em dupla.
# Hora de caprichar nas ideias.

# union(set2) ou |: Retorna um novo set que é a união de dois sets.


# Biblioteca
import os

# Limpando o terminal
os.system('cls')


print('=' * 50)
print('METODO UNION OU |')
print('-' * 50)

# declarando

# entrada
entrada1 = input('Entre com a 1ª lista que você desa unir separando cada elemento por ",": ')
entrada2 = input('Entre com a 2ª lista que você desa unir separando cada elemento por ",": ')

# processamento
# tranformando as entradas em listas
lista1 = entrada1.split(',')
lista2 = entrada2.split(',')
# Transformando em set
set1 = set(lista1)
set2 = set(lista2)
# unindo as duas lista
#unidas = set1.union(set2)

# corrigindo a sequencia com sort
#if int in entrada1 or entrada2:
#    sequencia = unidas.sort 

print(lista1)
print(set1)
print(lista2)
print(set2)