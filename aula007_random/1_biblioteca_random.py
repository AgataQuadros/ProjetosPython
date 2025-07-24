import random
import os


os.system

print('-' * 70)
print('BIBLIOTECA RANDOM')
print('-' * 70)

print('Número aleatório')
numero_aleatorio = random.random()
print(f'O número gerado foi: {numero_aleatorio}')


print('Número aleatório inteiro')
aleatorio_inteiro = random.randint(1,20)
print(f'O número inteiro gerado foi: {aleatorio_inteiro}')


print('Número aleatório decimal no intervalo')
aleatorio_decimal = random.uniform(1,10)
print(f'O número decimal gerado foi: {aleatorio_decimal}')

print('Sorteio em lista')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'O nome escolhido foi: {nome_sorteado}')

print('Embaralhar sequencia')
lista2 = ['Ágata', 'Coly', 'Isis', 'Bia']
print(f'Lista antiga: {lista2}')
#embaralhando = list(random.shuffle(lista)) dá erro
#embaralhamento = random.shuffle(lista) saida vazia
random.shuffle(lista2)
print(f'lista nova: {lista2}')
print('-' * 70)

print('Retorno de elementos únicos de uma população')
numeros = [1, 2, 3, 4, 5, 6, 7]
amostra_aleatoria = random.sample(numeros, 5)
print(f'Retorno da amostra {amostra_aleatoria}')
print('.' * 70)