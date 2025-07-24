import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS : LISTA []')
print('=' * 70)

lista_numeros_inteiros = [1,2,3,4]
lista_vogais = ['a','e','i','o','u']
lista_nomes = ['John','Jane','Carol']
lista_heterogenea = ['jhon',80,1.90,'AB']
lista_dentro_lista = [[1,2,3,4],['a','e','i','o','u']]

print(f'Lista de números: {lista_numeros_inteiros}')
print(f'Lista de vogais: {lista_vogais}')
print(f'Lista de nomes: {lista_nomes}')
print(f'Lista de mistura: {lista_heterogenea}')
print(f'Lista de lista: {lista_dentro_lista}')

# Varrendo os índices manualmente
lista_num_indice_0 = lista_numeros_inteiros[0]
lista_vogais_ind_1 = lista_vogais[1]
lista_nomes_ind_2 = lista_nomes[2]
lista_heterogenea_ind_3 = lista_heterogenea[3]
lista_num_indice_1 = lista_dentro_lista[1]

print('-' * 70)
print('Acessando os elementos de uma lista')
print('=' * 70)
print(f'Lista de números: {lista_num_indice_0}')
print(f'Lista de vogais: {lista_vogais_ind_1}')
print(f'Lista de nomes: {lista_nomes_ind_2}')
print(f'Lista de mistura: {lista_heterogenea_ind_3}')
print(f'Lista de lista: {lista_num_indice_1}')

print('-' * 70)
print('Fim do programa!')
print('-' * 70)