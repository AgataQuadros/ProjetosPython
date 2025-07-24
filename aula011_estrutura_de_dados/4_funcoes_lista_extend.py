import os


os.system('cls')

#inicialisa a lista vazia
lista_numeros = []

#solicitando ao usuario para inseris numeros separados por espaço
entrada = input('Digite números separados por espaço: ')

#divide a string de entrada um uma lista de strings
numeros = entrada.split()

#cria uma lista para armazenar os numeros pares
pares = []

#itera sobre os numeros inseridos
for numero in numeros:
    #converte a string para inteiro
    numero_aux = int(numero)
    #verifica se o numero é par
    if numero_aux % 2 == 0:
        #adiciona o numero para a lista principal
        pares.append(numero_aux)

#usa extend() para adicionar os numeros pares a lisa proncipal
lista_numeros.extend(pares)

print(f'Números pares adicionados á lista: {lista_numeros}')