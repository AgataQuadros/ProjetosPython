import os


os.system('cls')


# Definindo uma função
def caucular_velocidade_media(distancia, tempo):
    # Vm = ΔS/Δt
    velocidade_media = distancia / tempo
    return velocidade_media

distancia = float(input('Digite a distância em quilometro: '))
tempo = float(input('Digite o tempo gasto em horas: '))

# Calcular a valocidade media usando a unção criada
velocidade = caucular_velocidade_media(distancia, tempo)

# Exibir o resultado
print(f'A valocidade média é {velocidade:.2f} km/h.')