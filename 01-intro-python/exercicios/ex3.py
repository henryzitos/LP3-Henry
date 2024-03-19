# Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída
# o valor final com desconto e o desconto aplicado com base nas seguintes regras:
# Compras entre R$0,01 e R$9,99 - 0% de desconto
# Compras entre R$10,00 e R$99,99 - 5% de desconto
# Compras entre R$100,00 e R$499,99 - 10% de desconto
# Compras iguais ou superiores a R$500 - 15% de desconto

valorCompra = float(input("Digite o valor da compra: "))

if(valorCompra == 0):
    print("Você nem gastou dinheiro!")
elif(valorCompra >= 0.01 and valorCompra <= 9.99):
    desconto = 0.0
    valorComDesconto = valorCompra - (valorCompra * desconto)
    print(valorComDesconto, desconto * 100,"%")
elif(valorCompra >= 10.0 and valorCompra <= 99.99):
    desconto = 0.05
    valorComDesconto = valorCompra - (valorCompra * desconto)
    print(valorComDesconto, desconto * 100,"%")
elif(valorCompra >= 100.0 and valorCompra <= 499.99):
    desconto = 0.1
    valorComDesconto = valorCompra - (valorCompra * desconto)
    print(valorComDesconto, desconto * 100,"%")
elif(valorCompra >= 500.0):
    desconto = 0.15
    valorComDesconto = valorCompra - (valorCompra * desconto)
    print(valorComDesconto, desconto * 100, "%")
else:
    print("Erro")
