import os


os.system('cls')

# Definindo função
def dados_paciente(nome='Coly', nascimento=2005, peso=46, altura=1.68):
    print(f'Bem vindo(a) ao sistema do senac {nome}')
    print(f'O ano de nascimento de {nome} é {nascimento}')
    print(f'O peso de {nome} é {peso}kg')
    print(f'A altura de {nome} é {altura}m')
    print('-' * 70)

# Inicio para lembrar
def posicional_nomeado(nascimento, nome='Coly'):
    print(f'Bem vindo(a) ao sistema do senac {nome}')
    print(f'O ano de nascimento de {nome} é {nascimento}')
    print('-' * 70)


#def nomeado_posicional(nome='Coly', nascimento): # Não funciona
#    print(f'Bem vindo(a) ao sistema do senac {nome}')
#    print(f'O ano de nascimento de {nome} é {nascimento}')
#    print('-' * 70)
# fim para lembrar


#invocando função
dados_paciente()

dados_paciente(nome='Isis', nascimento=1985, peso=46, altura=1.68)
dados_paciente(nascimento=2008, nome='Ágata',  peso=46, altura=1.68)
dados_paciente(altura=1.68, peso=46, nome='Bia',nascimento=2008)