import os

from pacote1.modulo_somar import somar
from pacote1.subpacote.modulo_multiplicar import multiplicar as multi
from pacote1.modulo_dividir import dividir

while True:
    os.system('cls')

    a = input('entre com o valor de A: ')
    b = input('entre com o valor de B: ')

    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        print('Por favor, entre com um número válido.')
        continue
    a = float(a)
    b = float(b)

    resultado_soma = somar(a, b)
    resultado_produto = multi(a,b)
    resultado_divisao, erro = dividir(a, b)
    