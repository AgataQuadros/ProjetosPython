import math
import os


os.system('cls')

print('-' * 50)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')
print('-' * 50)
print()

#Entrada de dados
numero_decimal = float(input('Entre com o número decimal: '))

#Processamento
arredonda_pra_cima = math.ceil(numero_decimal)
arredonda_pra_baixo = math.floor(numero_decimal)

#Saída
print('')
print(f'o numero decimal {numero_decimal} arredondado' 
      f'para cima é: {arredonda_pra_cima}')
print(f'o numero decimal {numero_decimal} arredondado' 
      f'para baixo é: {arredonda_pra_baixo}')
print('-' * 50)