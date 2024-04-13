'''
Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da 
forca. O programa começa com uma palavra oculta (o usuário não vê) 
e o usuário tenta adivinhar a palavra, letra por letra. O usuário 
tem um número limitado de tentativas para adivinhar toda a palavra.
'''
letraPorLetra = list()
tamanhoDaPalavra = 0
i = 0
j = 0
palavra = " "

def gerencia_palavra():
    global letraPorLetra
    global tamanhoDaPalavra
    global palavra
    
#    palavra = input("Digite uma palavra: ")
#    palavra = palavra.strip()

    palavra = "Banana"
    tamanhoDaPalavra = len(palavra)
    for letra in palavra:
        letra = letra.capitalize()
        letraPorLetra.append(letra)

letrasDescobertas = list()
    
def exibe_as_letras():
    global letraPorLetra
    global letrasDescobertas
    
    if i == tamanhoDaPalavra:
        print("Parabéns! Você ganhou o jogo.")
        for letra in letraPorLetra:
            if letra in letrasDescobertas:
                print(letra, end = " ")
        print("| A palavra era: " + palavra)
        exit()
        
    for letra in letraPorLetra:
        if letra in letrasDescobertas:
            print(letra, end = " ")
        else:
            print("_", end = " ")
    chute()
            
def chute():
    global letraPorLetra
    global letrasDescobertas
    global i
    global tamanhoDaPalavra
    global j

    if j == 0:
        print("Vamos começar o jogo!")
        j += 1
        exibe_as_letras()

    letraAdvinha = input("Digite a letra: ")
    letraAdvinha = letraAdvinha.capitalize()
        
    if letraAdvinha in letraPorLetra:
        j = 0
        if letraAdvinha in letrasDescobertas:
            print("Você já digitou essa letra.")
            exibe_as_letras()
        elif letraAdvinha not in letrasDescobertas:
            print("Você acertou uma letra!")
            letrasDescobertas.append(letraAdvinha)
            while j < tamanhoDaPalavra:
                if letraAdvinha == letraPorLetra[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
        exibe_as_letras()
    else:
        print("Essa letra não está na palavra! Tente novamente.")
        chute()
            
gerencia_palavra()
chute()
