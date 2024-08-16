# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 13/08/2024

# Biblioteca
import os


# Limpando o terminal
os.system('cls')


print("Hi! my name dosen't meter, but yours do. How are you called sweet being?")
empresta_pra_aquilo = input("the voice asks for your name, do you lend it to it?... ")
 
if 'yes' in empresta_pra_aquilo:
    seu_nome = input("what is your name?... ")
elif 'no' in empresta_pra_aquilo:
    print("Smart little thing.")
    print("But i still have to call you something..")
    print("I'll just keep calling you little one")

print(f"So, {seu_nome} what do you think about and adventure?")
aceitar = input('do you want this?... ')