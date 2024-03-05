# - Identificadores
# letra, número e _
# palavras reservadas: def, if, for...
# case sensitive

# - Variáveis
# identificador = valor (literal)
# tipagem dinâmica

# - Constantes
# python não tem constante, sendo assim...
# coloque o nome inteiro da constante em maiúsculo

# comentário de única linha
'''
    Comentário de 
    múltiplas linhas
'''

# - docstring
# documentação de código de funções, classes, módulos, etc.

def somar(n1, n2):
    '''
    Função que soma dois números

    :param n1: primeiro número
    :param n2: segundo número
    :return: a soma dos parâmetros
    '''
    return n1 + n2

somar(9.5, 0.5)
# somar("Henry", True)
