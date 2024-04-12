'''
Ex08 - Função de Contagem de Palavras: Escreva uma função que receba 
uma string (frase) como argumento e retorne um dicionário onde as 
chaves são as palavras únicas no texto e os valores são o número de 
vezes que cada palavra aparece no texto. Depois, teste a função com 
diferentes textos fornecidos pelo usuário.
'''

frase = input("Digite uma frase: ")
print(frase)
palavra = ""
dicionario = {}

for letra in frase:
    if letra.isalpha() == False:
        for key in dicionario:
            if key == palavra:
                print("Palavra repetida.")
                print(palavra)
            else:
                print(palavra)
                print("Adicionando palavra ao dicionario")
        palavra = ""
    elif letra.isalpha():
        palavra = palavra + letra
        print(palavra)
