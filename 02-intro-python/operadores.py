# Operadores artimeticos
# +, -, *, /, **
nota1 = 10.0
nota2 = 5.5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3

if media >= 6.0:
    print("Aprovado")

# potenciação 
# n elevado a e | ex: 10 eleveado a 2
n = 10
numero_elevado = n ** 2

# Operadores lógicos
# and, or, not

print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

print(not True)        # False
print(not False)       # True

# permitir entrada quando/se 
# - o usuário for funcionário 
# - o usuário não estiver bloqueado
# - hora atual estiver entre 8h e 18h

# permitir entrada
# - admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False

horario_comercial = hora_atual >= 8 and hora_atual <= 18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado

if usuario_admin or (funcionario_ativo and horario_comercial):
    print("Entrada permitida.")

# Operadoes de comparação
# ==, !=, >, <, >=, <=

idade = 25
maior_idade = idade >= 18

if media >= 6.0:
    print("Aprovado")

# is, is not
# operador de identidade
# compara se os objetos ocupam o mesmo espaço de memória

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # Compara os valores | True
print(a is b) # False

# operaodr in, not in
# verificar se um elemento existe ou não em uma sequência
# str, list, tuple
opcoes = ("Sim", "Não", "Talvez")
# * criação de dicts
opcao = input("Digite uma opção: ")

opcao = opcao.strip()
opcao = opcao.capitalize()

if opcao in opcoes:
    print("Essa opção existe")
else:
    print("Não existe essa opção")
