import os


os.system('cls')

print('-' * 70)
print('Operadores úteis para')
print('Srings e Estrutras de Dados')
print('=' * 70)

texto = 'Ola, Mundo!'

print(f'Texto: {texto}')
if 'Mundo' in texto: # Verifica a palavra dentro da string
    print('Apalavra "mundo" esta presente na string')
else:
    print('Apalavra "mundo" não esta presente na string')

print('.' * 70)

texto2 = 'Ola, Python!'

print(f'Texto 2: {texto2}')
if 'Mundo' not in texto2: # Verifica a palavra dentro da string
    print('Apalavra "mundo" não esta presente na string')
else:
    print('Apalavra "mundo" esta presente na string')

print('-' * 70)