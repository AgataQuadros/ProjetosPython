import os


os.system('cls')


# Definindo função
def multiplicar(a, b=1):
    return a * b


resultado_1 = multiplicar(5)
resultado_2 = multiplicar(5, 2)

print(f'O 1º resultado é {resultado_1}')
print(f'O 2º resultado é {resultado_2}')
print()