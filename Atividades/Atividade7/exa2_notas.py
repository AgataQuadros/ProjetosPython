# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas. 
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.


# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO B')
print('-' * 20)

# Declaração
notas = []
soma = 0
media = 0
contador = 0

# Entrada
while True:
    notas.append(int(input(f' Entre com a nota do aluno: ')))
    contador += 1 # conta as notas
    if 0 in notas:
        break

# Processamento
for nota in notas: #soma das notas
    soma += nota

media = soma / 4 #media das notas

notas2 = notas.copy()
lista_inversa = notas2.reverse()

# Saida
print('Qwantidade de notas:')
print(contador)
print('Soma das notas:')
print(soma)
print('Media das notas:')
print(media)
print('Lista das notas:') 
print(notas)
print('Lista das notas inversa:') 
print(notas2)