import csv
import os

# Nome do arquivo CSV
arquivo = 'arquivos_csv/gravacao/alunas.csv'
nome_para_alterar = input('Digite o nome que deseja alterar: ')

# Lendo dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)

# Verificando se o nome existe e permitindo a alteração do registro
alterado = False
for registro in cadastro:
    if registro['nome'] == nome_para_alterar:
        print(f"Registro encontrado: {registro}")
        informacao_para_alterar = input('Qual informação você deseja alterar (nome, telefone, cidade, todos)?: ').lower()
        
        if informacao_para_alterar == 'nome':
            registro['nome'] = input('Digite o novo nome: ')
            alterado = True
        elif informacao_para_alterar == 'telefone':
            registro['telefone'] = input('Digite o novo telefone: ')
            alterado = True
        elif informacao_para_alterar == 'cidade':
            registro['cidade'] = input('Digite a nova cidade: ')
            alterado = True
        elif informacao_para_alterar == 'todos':
            registro['nome'] = input('Digite o novo nome: ')
            registro['telefone'] = input('Digite o novo telefone: ')
            registro['cidade'] = input('Digite a nova cidade: ')
            alterado = True
        else:
            print("Informação inválida. Tente novamente.")
        
        break

# Reescrevendo o arquivo com os dados atualizados, se houve alteração
if alterado:
    with open(arquivo, 'w', newline='') as arquivo_csv:
        campos = ['nome', 'telefone', 'cidade']
        escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
        
        escrever.writeheader()
        escrever.writerows(cadastro)
    print('-' * 70)
    print(f'Registro com nome {nome_para_alterar} alterado com sucesso.')
else:
    print('-' * 70)
    print(f'Registro com nome {nome_para_alterar} não encontrado ou nenhuma alteração foi feita.')
print('-' * 70)