'''
Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite 
uma palavra ou frase e verifique se é um palíndromo (ou seja, pode 
ser lida de frente para trás e de trás para frente da mesma forma).
'''

def verificaPalindromo(palavra):
    palindromo = palavra[::-1] 
    if palavra == palindromo:
        print("Sua palavra é um palindromo")
    else:
        print("Sua palavra não é um palindromo")
        
palavra = input("Digite uma palavra: ")
verificaPalindromo(palavra)
