# importar a biblioteca csv
import csv
import os


# Criando uma lista de dicionario: cada dicionario é uma linha (registro)

lista = [
        {'nome' : 'Agata', 'telefone' : '(32)99196-0000', 'cidade' : 'Juiz de Fora'},
        {'nome' : 'Bia', 'telefone' : '(32)99196-1111', 'cidade' : 'Juiz de Fora'},
        {'nome' : 'Coly', 'telefone' : '(32)99196-2222', 'cidade' : 'Juiz de Fora'},
        {'nome' : 'Isis', 'telefone' : '(32)99196-3333', 'cidade' : 'Juiz de Fora'},
         ]

# Caminho para a pasta onde o arquivo cvs sera salvo
pasta = 'arquivos_csv/gravação/'

# Verificando se a pasta existe, se não irá cria-la
os.makedirs(pasta, exist_ok=True)

# Nome para o arquivo csv gravar informações
arquivo = 'arquivos_csv/gravação/alunas.csv'

# Caminho completo do arquivo csv
caminho_arquivo = os.path.join(pasta, arquivo)

# Abra o arquivo 'arquivo' no modo de escrita ('w').
# Se o arquivo não existir, ele sera criado; se existir, sera truncado(esvaziado).
# newline='': Evita a adição de linhas em branco extra ao gravar o arquivo em algumas plataformas
# as arquivo_cvs: Atribui o objeo arquivo ao 'arquivo_csv' para ser usado dentro do bloco with
with open(arquivo, 'w', newline='')as arquivo_csv:
    # campos = ['nome', 'telefone', 'cidade']: Define a lista de nomes de campos
    #cabeçalho das colunas do csv
    campos = ['nome', 'telefone', 'cidade']

    # write = csv.DictWriter(arquivo_csv, fieldnames=campos):
    # Cria um objeto DictWriter queusara 'arquivo_csv' para gravar os campos.
    # fieldnames define a ordem dos campos no arquivo csv.
    # delimiter=';': é o separador
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')

    # write.writeheader(): Gravar todas as linhas de cabeçalho no
    # arquivo csv usando os nomes de campos definidos em fieldnames.
    escrever.writerows(lista)

os.system('cls')
# Exibe uma mensagem indicando que o arquivo foi gravado com sucesso.
print(f'Arquivo {arquivo} gravado com sucesso!')