'''
Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba 
a tabuada desse número de 1 a 10.
'''

def exibeTabuada(numero):
    i = 1
    while(i <= 10):
        print("%d * %d = %d" % (numero, i, numero * i))
        i = i + 1
        # print('a={:d}, b={:d}'.format(f(x,n),g(x,n)))

numero = int(input("Digite um número para ver sua tabuada de 1 a 10: "))
exibeTabuada(numero)
