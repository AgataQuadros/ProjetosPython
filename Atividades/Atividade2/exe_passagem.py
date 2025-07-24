# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO E')
print('-' * 20)

# Entrada

passagem1 = 0.70
passagem2 = 0.40
resposta = ''
km = int(input('entre com a distancia que você percorrerá em km: '))

# Processamento
if km > 200:
    pagar = km * 0.40
    resposta = f'com a distancia {km} voce pagará {pagar}'
else:
    pagar = km * 0.70
    resposta = f'com a distancia {km} voce pagará {pagar}'

# Saída
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('fim do exercício')
print('=' * 50)