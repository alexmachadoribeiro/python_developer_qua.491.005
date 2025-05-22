"""
Programa que irá receber do usuário dois números reais e o usuário irá escolher uma das quatro operações básicas da matemática, e o programa irá calcular com base na escolha do usuário e informar o resultado.
"""
# TODO

# declaração de variáveis
x = float(input("Informe o valor de X: ").replace(",", "."))
y = float(input("Informe o valor de Y: ").replace(",", "."))

# menu
print(f"{'-'*20} CALCULADORA PYTHON {'-'*20}")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão\n")

operador = input("Informe a opção desejada: ")

# verifica a operação escolhida e faz o cálculo
match operador:
    case "1":
        print(f"O resultado da soma é: {x+y}.")
    case "2":
        print(f"O resultado da subtração é: {x-y}.")
    case "3":
        print(f"O resultado da multiplicação é: {x*y}.")
    case "4":
        print(f"O resultado da divisão é: {x/y}.")
    case _:
        print("Operador inválido.")