#importando biblioteca
import os
import math



#limpar terminal
os.system('cls')

print('-' * 70)
print('ESTUDO DA BIBLIOTECAMATEMATICA MATH')
print('=' * 70)

# declarações
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5 #caeto oposto
ca= 10 #cateto adjecente

#processamento
potencia = math.pow(base, expoente)
raizquadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

#saida
print(f'{base} elevado a {expoente} é igual a: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizquadrada}')
print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseno:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')
print(f'-' * 70)