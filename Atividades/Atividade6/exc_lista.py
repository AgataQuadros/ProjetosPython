# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9 x
# • O intervalo de 8 até 13 x
# • Os números pares x
# • Os números ímpares x
# • Os múltiplos de 2, 3 e 4 x
# • Lista reversa x
# • O produto dos intervalos 5-6 por 11-12


# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO C')
print('-' * 20)


# Entrada
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista_numeros_2 = lista_numeros.copy()
pares = []
impar = []
multiplos_3 = []
multiplos_4 = []
resultado = []

# Processamento
lista_09 = lista_numeros[0:9]
lista_813 = lista_numeros[7:13]
lista_numeros_2.reverse() # lista eversa/lista decrescente

for numero in lista_numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impar.append(numero)

for item in lista_numeros:
    if item % 3 == 0:
        multiplos_3.append(item)


for item in lista_numeros:
    if item % 4 == 0:
        multiplos_4.append(item)

for intervalo_a in lista_numeros[4:6]:
    for intervalo_b in lista_numeros[10:12]:
        produto = intervalo_a * intervalo_b
        resultado.append(produto)




# Saída
print('lista de 0 a 9:')
print(lista_09)
print('lista de 8 a 13:')
print(lista_813)
print('Lista invertida:') 
print(lista_numeros_2)
print(f'Lista de Pares:')
print(pares)
print(f'Lista de Impares:')
print(impar)
print('lista de multiplos de 2:')
print(pares)
print('lista de multiplos de 3:')
print(multiplos_3)
print('lista de multiplos de 4:')
print(multiplos_4)
print('lista do produto entre os intervalos 5,6 x 11,12:')
print(resultado)

