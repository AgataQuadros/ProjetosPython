import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS : LISTAS [ ]')
print('=' * 70)

soma = 0

# criando uma lista
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

#percorrendo a lista com o enumarate()
#o comando enumarate adiciona um indice
#para cada valor da nossa lista
#start opcional, para não começar no indice 0
#enumarate(listaNumeros, start=1)

# Para cada número dentro da lista de números, enumere com um indice
for indice, numero in enumerate(lista_numeros):
    soma += numero #soma os numeros
    print(f'Indice: {indice} = Número: {numero}')

print('-' * 70)
print('Fim do programa!')
print('-' * 70)
