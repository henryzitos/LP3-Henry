# if
idade = 60

if idade >= 18:
    print("Maior de idade")

# if/else
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# if/elif/else
if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
elif idade > 59:
    print("Idoso")
else:
    print("Ué meu Deus")

# condições aninhadas
email = "user@gmail.com"
senha = "123"

if (email == "user@gmail.com" and senha == "123"):
    print("Liberado")
else:
    print("Erro")

def liberar_acesso(email, senha):
    '''
    if (email == "user@gmail.com" and senha == "123"):
        print("Liberado")
        return True
    else:
        print("Erro")
        return False
    '''
    return email == "user@gmail.com" and senha == "123"

def dentro_horario_comercial(hora_atual):
    return hora_atual >= 8 and hora_atual <= 18

# dia       1, 2, 3, 4, 5, 6, 7
# palavra   domingo, segunda, terça, quarta, quinta, sexta, sábado, domingo

dia = 2

dias = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
}
# keys e values de sets

if dia in dias:
    print(dias[dia])