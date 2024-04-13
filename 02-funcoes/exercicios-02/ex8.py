'''
Ex08 - Função de Contagem de Palavras: Escreva uma função que receba 
uma string (frase) como argumento e retorne um dicionário onde as 
chaves são as palavras únicas no texto e os valores são o número de 
vezes que cada palavra aparece no texto. Depois, teste a função com 
diferentes textos fornecidos pelo usuário.
'''

def contar_palavras(frase):
    dicionario = {}
    palavras = frase.split()
    
    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    
    return dicionario

frase = input("Digite uma frase: ")
resultado = contar_palavras(frase)
print(resultado)