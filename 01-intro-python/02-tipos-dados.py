# - Tipos de dados
# int, float
# string, list, tuple, set
# dict
# None

# int
idade = 20
temperatura = -30

# float
altura = 1.55
PI = 3.14

# string
nome_um = "Arthur Lessa"
nome_dois = 'Henry Zitos'
# char (?)
letra = 'a'

print(nome_um[0])
print(nome_um[-5])

# str tem métodos 
print(nome_um.upper())

# interpolação de str e variáveis
# f-string
nome = "Arthur"
idade = 16
mensagem = f"Olá {nome}. Você tem {idade} anos."
print(mensagem)

# list
# lista de valores, pode ser alterada
habilidades = []
habilidades = ["Java", "React", "C++"]
print(habilidades)
print(habilidades[2])
habilidades[2] = "JavaScript"
habilidades.append("CSS")
habilidades.insert(0, "HTML")
print(habilidades)

# tupla
# "lista" de valores, não pode alterar (adicionar/remover)
opcoes = ("Sim", "Não", "Talvez")

# for
for opcao in opcoes:
    print(opcao)

for habilidade in habilidades:
    print(habilidade)

# set
# não indexado
# não permite elementos duplicados
# Digite a mensagem 
# Digite os emails de destino
# tutu@gmail.com
# henreco@hotmail.com
emails = {'tutu@gmail.com', 'henreco@hotmail.com', 'tutu@gmail.com'}
emails.add('tutu@gmail.com')
print(emails)

# dict (dicionário)
# chave : valor / key : value

# site de emprego
# empresa = "Google"
# titulo = "Engenheiro de Software"
# salario = 20000.00
# remoto = False

# vaga
vaga = {
    'empresa': 'Google',
    'titulo': 'Engenheiro de Software',
    'salario': 20000.00,
    'remoto': False
}

print(vaga['salario'])

# None
nome = None

def gerar_boletim(prontuario):
    # se encontrou o aluno(a) no bd
    return 'boletim'
    #else
    return None