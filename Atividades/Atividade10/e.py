# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Objetivo: Crie uma função que receba a altura e o peso de uma pessoa.
# Depois retorne o seu IMC.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO E')
print('-' * 20)

#Processamento
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Entrada
peso = float(input('Entre com o seu peso em kg(ex: 64): '))
altura = float(input('Entre com a sua autura em m(ex: 1.50): '))

# Saida

imc = calcular_imc(peso, altura)
print(f"IMC: {imc:.2f}")

if imc <= 18.5:
    print('Você esta abaixo do peso :(')
elif imc <= 25:
    print('Você temo peso normal :D')
elif imc <= 30:
    print('Você esta em sobrepeso :(')
else:
    print('Você esta em alto sobrepeso :(')


# Abaixo do peso: IMC menor que 18,5
#Peso normal: IMC entre 18,5 e 24,9
#Sobrepeso: IMC entre 25 e 29,9
#Obesidade grau I: IMC entre 30 e 34,9
#Obesidade grau II: IMC entre 35 e 39,9
#Obesidade grau III(obesidade mórbida): IMC igual ou superior a 40