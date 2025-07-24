import os


os.system('cls')

print('-' *70)
print('Fatiamento de Strings')
print('-' *70)

frase = 'String em Python!'

# Exibindo a string original
print(f"String Original: {frase}")

# Fatiamento: acessando partes específicas da string
# Primeiros cinco caracteres
primeiros_cinco = frase[:5]
print(f"Primeiros Cinco Caracteres: {primeiros_cinco}")

# Ultimos dez carateres
ultimos_dez = frase[-10:]
print(f"Últimos Dez Caracteres: {ultimos_dez}")

# Do quarto ao décimo caractere
quarto_ao_decimo = frase[3:10]
print(f"Do Quarto ao Décimo Caractere: {quarto_ao_decimo}")

# A cada dois caracteres
a_cada_dois = frase[::2]
print(f"A Cada Dois Caracteres: {a_cada_dois}")

# invertendo a string
invertida = frase[::-1]
print(f"String invertida: {invertida}")
print()