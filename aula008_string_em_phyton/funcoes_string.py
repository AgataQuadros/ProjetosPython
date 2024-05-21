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

















