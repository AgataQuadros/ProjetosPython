import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE: CONTINUE')
print('=' * 70)

print()

for c in range(1, 11):
    if c == 5:
        # 5 está fora do loop, se retirar a proxima linha
        # ele não vai aparecer
        print(f' O número {c} esta fora do loop')
        continue
    
    print(f' o número é {c}')
    
print('-' * 70)
print()