'''
Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar
uma frase e retorne o número de vogais e consoantes na frase.
'''

i = 0
j = 0

def aLetraEh(frase):
    global i
    global j
    for letra in frase:
        if(letra.isalpha()):
            letra = letra.capitalize()
            if(letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
                i = i + 1
            else:
                j = j + 1
            
frase = input("Digite uma frase: ")
frase = frase.strip()

aLetraEh(frase)

print("Quantidade de vogais = %d" % (i))
print("Quantidade de consoantes = %d" % (j))
