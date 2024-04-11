'''
Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação
fornecida pelo usuário (0 a 100), converta para o sistema de notas A,
B, C, D, ou F, seguindo os padrões de conversão comuns.
'''

def recolheNota():
    nota = float(input("Digite a nota em número (0 a 100): "))
    if (nota > 100 or nota < 0):
        while(nota > 100 or nota < 0):
            nota = double(input("Digite uma nota em número válida! (0 a 100): "))
    return nota

def conversorDeNota(nota):
    if nota == 0:
        return "F"
    elif (nota >= 1 and nota <= 35):
        return "D"
    elif (nota >= 36 and nota <= 60):
        return "C"
    elif (nota >= 61 and nota <= 85):
        return "B"
    elif (nota >= 86 and nota <= 100):
        return "A"
    else:
        print("Erro")
        
nota = float(recolheNota())
notaConvertida = conversorDeNota(nota)

print("Nota em números = %.2f | Nota convertida é: %s" % (nota, notaConvertida))
        
    
