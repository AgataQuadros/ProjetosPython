# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 13/08/2024

# Biblioteca
import os


# Limpando o terminal
os.system('cls')


# entrada

nome = input('Entre com o seu nome: ')
genero = input('Entre com seu gênero (f- feminino, m- masculino, o- outro): ')
print('por ser um codigo raso não avera muitas mudanças nos generos das palavras mesmo que você informe o seu genero!!')
print('concertaremos isso em atualizações futuras!')

if 'o' in genero:
    qual = input('Qual é o seu genero?(s- não quero informar): ')

    if 's' in qual:
        print('Ok! vamos continuar')

