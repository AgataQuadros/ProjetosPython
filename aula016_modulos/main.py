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
    
    print('-' * 70)
    print('CÁLCULOS MATAMÁTICOS')
    print('=' * 70)
    print(f'Cáuculo da soma: {resultado_soma}')
    print(f'Cáuculo do produto: {resultado_produto}')
    print(f'Cáuculo da divisão: {resultado_divisao}, {erro}')
    print('-' * 70)

    sair = input('Deseja sair do programa? (s/n): ').strip().lower()
    if sair == 's':
        print('Saindo do programa... ')
        break