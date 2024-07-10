# SE O USUARIO DER M/S AO ENVES DE KM/H

import os


os.system('cls')


# definindo
lista_suporte = []

# Definindo uma função
def caucular_velocidade_media(distancia, tempo):
    # Vm = ΔS/Δt
    velocidade_media = distancia / tempo
    return velocidade_media

distancia = int(input('Digite a distância : '))
simbolo_dist = input('me diga se a distancia esta em Km(quilometros) ou m(metros): ')
tempo = int(input('Digite o tempo gasto: '))
simbolo_tempo = input('me diga se a distancia esta em h(horas),min(minutos) ou s(segundos): ')


# Calcular a valocidade media usando a unção criada
velocidade = caucular_velocidade_media(distancia, tempo)

if 'km' in simbolo_dist:
    if 'h' in simbolo_tempo:
        print(f'A valocidade média é {velocidade:.2f} km/h.')

    elif 'min' in tempo:
        print(f'')

#    elif 's' in tempo:

#if 'm' in distancia:
#    if 'h' in tempo:
    
#    elif 'min' in tempo:

#    elif 's' in tempo:












# Exibir o resultado
#