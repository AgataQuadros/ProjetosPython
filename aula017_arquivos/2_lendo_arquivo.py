import csv
import os


# Nome do arquivo csv
arquivo = 'arquivos_csv/gravacao/alunas.csv'

# Lista para armazenar os dados
lista = []

# Abrindo o arquivo csv para leitura
with open(arquivo, 'r') as arquivo_csv:
    # Criando u  leitor de csv que lê o arquivo como dicionario
    leitura = csv.DictReader(arquivo_csv, delimiter=';')

    # Iterando sobre cadalinha (registro) no arquivo csv e adcionar a lista
    for linha in leitura:
        lista.append(linha)

os.system('cls')
print('-' * 70)
print('nome\ttelefone\tcidade')
print('=' * 70)

# Exibindo a lista resultante
for registro in lista:
    flag = 0
    for k, v in registro.items():
        print(v, end = '\t')
        flag += 1
        if flag == 3:
            print()

print('-' * 70)