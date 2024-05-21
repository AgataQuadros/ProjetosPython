import os


os.system('cls')

print('-' * 70)
print('Funções String')
print('-' * 70)

frase1 = 'Ola, Mundo!'
quantidade_de_caracteres = len(frase1) # conta os characteres
print(f'A frase {frase1} \n contem {quantidade_de_caracteres} caracteres')
print('-' * 70)

minunculas = frase1.lower() # frase em minúsculo
print(f'Frase original: {frase1}')
print(f'Frase nova: {minunculas}')
print('-' * 70)

maiuscula = frase1.capitalize() # frase capitalizada/maiuscula
print(f'Frase original: {frase1}')
print(f'Frase nova: {maiuscula}')
print('-' * 70)


frase2 = '   Ola, Mundo   '
sem_espacos = frase2.strip() # frase sem espaços
print(f'Frase original: {frase2}')
print(f'Frase nova: {sem_espacos}')
print('-' * 70)

substituto = frase2.replace('Mundo', 'Python') # frase substituida
print(f'Frase original: {frase2}')
print(f'Frase nova: {substituto}')
print('-' * 70)

lista = frase2.split(',') # frase em lista
print(f'Frase original: {frase2}')
print(f'Frase nova: {lista}')
print('-' * 70)

lista2 = ['Ola' , 'Mundo']
juncao = '-'.join(lista2) # frase unida de uma lista
print(f'Frase original: {lista2}')
print(f'Frase nova: {juncao}')
print('-' * 70)