# biblioteca
import math

# funções
def equacao_1o_grau(a, b): # type: ignore
    x = -b/a # type: ignore
    return x # type: ignore

def equacao_2o_grau(a, b, c): # type: ignore
    # a*x²+b*x+c = 0
    delta = (b**2)-(4*a*c) # type: ignore
    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a) # type: ignore
        x2 = (-b-math.sqrt(delta))/(2*a) # type: ignore
        yield f"x' = {x1}"
        yield f'x" = {x2}'
    elif delta == 0:
        x = -b/(2*a) # type: ignore
        yield f"x = {x}"
    else:
        yield "Não há raízes reais."

"""
# TODO - Crie um programa que calcule a equação do 1º grau.
# NOTE - Coloque um menu para o usuário decidir se quer calcular a equação ou sair do programa.
# NOTE - Coloque no menu a opção de calcular a equação do 2º grau (não precisa desenvolver essa função por enquanto).
# NOTE - Faça usando o conceito de módulo recém-ensinado, usando o comando 'import equacoes' no main.py.
"""