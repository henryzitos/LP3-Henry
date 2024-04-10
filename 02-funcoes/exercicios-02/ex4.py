'''
Ex04 - Simulador de Eleições
'''

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

def votacao():
    global votos_candidato1, votos_candidato2, votos_candidato3
    votos_candidato1 = 0 
    votos_candidato2 = 0
    votos_candidato3 = 0
    i = 0
    while (i < 5):
        print("--  Digite o número do seu candidato --")
        voto = int(input("1 - Fulano | 2 - Sicrano | 3 - Beltrano\n"))
        if(voto == 1 or voto == 2 or voto == 3):
            i = i + 1
            if(voto == 1):
                print("Voto para Fulano")
                votos_candidato1 += 1
            elif(voto == 2):
                print("Voto para Sicrano")
                votos_candidato2 += 1
            elif(voto == 3):
                print("Voto para Beltrano")
                votos_candidato3 += 1
            else:
                print("Erro")
    print("Votação finalizada.")
    
def comparacao():
    if(votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3):
        print("O candidato Fulano ganhou!")
    elif(votos_candidato2 > votos_candidato1 and votos_candidato2 > votos_candidato3):
        print("O candidato Sicrano ganhou!")
    elif(votos_candidato3 > votos_candidato1 and votos_candidato3 > votos_candidato2):
        print("O candidato Beltrano ganhou!")
    else:
        print("Houve um empate! Um novo turno ocorrerá.")
        votacao()
        comparacao()
        
votacao()
comparacao()
