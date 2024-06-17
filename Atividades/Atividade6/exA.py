# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Crie a lista [1, 2, 3, 5, 6] 
# e depois insira 
# o valor que está faltando na posição correta.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
print('-' * 20)


# Entrada
lista = [1, 2, 3, 5, 6]

print(f'A lista {lista} esta faltando um número')
numero = int(input('Qual número esta faltando?(digite apenas o número): '))
posicao = int(input('Em qual psição ele se encaixa?(digite apenas o número): '))

# Processamento
if posicao == 3  and numero == 4:
    lista.insert(posicao, numero)
    print()
    print('Parabens!! você corrigiu a lista!!')
    print('Lista após a correção:', lista)