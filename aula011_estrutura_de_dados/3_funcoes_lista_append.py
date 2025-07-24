import os


os.system('cls')

#inicializa uma lista vazia
lista_numeros = []

# Pede o ususario para inserir 3 N
for i in range(3):
    numero = int(input('Digite um número: '))
    #adiciona o N a lista
    lista_numeros.append(numero)

#Verifica se o numero esta na lista e 
#exibe uma mensagem correspondente
print('-----')
numero_verificar = int(input('Digite um número: '))

if numero_verificar in lista_numeros:
    print(f'O número {numero_verificar} esta na lista!')
else:
    print(f'O número {numero_verificar} não esta na lista!')