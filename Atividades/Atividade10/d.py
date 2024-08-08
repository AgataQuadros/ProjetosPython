# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Crie uma função que receba uma temperatura 
# em fahrenheit e retorne o valor em graus célsius.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)


def fahre_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


entrada_fahrenheit = int(input('entre com o grau em fahrenheit: '))
c = fahre_celsius(entrada_fahrenheit)

print(f'\nA temperatura {entrada_fahrenheit}ºF em Celsius é {c}ºC')