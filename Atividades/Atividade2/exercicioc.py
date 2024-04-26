# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 25/04/2024

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO C')
print('-' * 20)

# Entrada
velocidade = int(input('digite a velocidade: '))
velocidade_certa = int(60)
resposta = ''

# Processamento
if velocidade > velocidade_certa:
    resposta = 'Ah não! você esta indo acima da velocidade permitita :('
else:
    resposta = 'Muito bem! você esta correndo conforme as leis de transito :D'

# Saída
print('')
print('-' * 20)
print(resposta)
print('-' * 20)
print('fim do exercício')
print('=' * 50)