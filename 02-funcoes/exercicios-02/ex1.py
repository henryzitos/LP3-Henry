'''
Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar 
um número entre 1 e 100 que o programa escolheu aleatoriamente.
Informe ao usuário se o palpite está alto ou baixo, até que ele
acerte o número.
'''

import random

def numeroAleatorio():
    numero_aleatorio = random.randint(1, 100)
    return numero_aleatorio

def advinharNumero():
    numeroAdvinhar = numeroAleatorio()
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == numeroAdvinhar:
                print("Você ganhou!")
                break
            elif numero > numeroAdvinhar:
                print("Seu palpite foi alto! Tente novamente")
            elif numero < numeroAdvinhar:
                print("Seu palpite foi baixo! Tente novamente")
        except ValueError:
                print("Isso não é um número válido. Tente novamente.")

advinharNumero()
