# for
palavra = "Python"
for letra in palavra:
    print(letra)

numeros = [1, 3, 4, 6, 8]
for numero in numeros:
    print(numero)

# range
# range(stop)
range(5) # 0, 1, 2, 3, 4
# range(start, stop)
range(1, 10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
#range(start, stop, step)
range(2, 20, 2) # 2, 4, 6, 8, 10, 12, 14, 16, 18

# len - quantidade de elementos

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

numeros = [1, 3, 5, 7, 8, 10]
# break pula o loop
# encontrar o primeiro numero par e parar
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break

print("Divisor")
# continue
# pula a iteração
for numero in numeros:
    if numero <= 5:
        continue
    print(numero)

# compreensão de lista
numeros = [2, 4, 6]
quadrados = []

for numero in numeros:
    quadrados.append(numero * numero) # numero ** 2
'''
for quadrado in quadrados:
    print(quadrado)
'''
quadrados = [numero ** 2 for numero in numeros]

numeros = [1, 3, 5, 6, 7, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
'''
for par in pares:
    print(par)
'''
pares = [numero for numero in numeros if numero % 2 == 0]

palavras = ["olá", "mundo", "python"]
palavras2 = [palavra.capitalize() for palavra in palavras]
for palavra in palavras2:
    print(palavra)