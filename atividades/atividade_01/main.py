"""
Crie um programa que receba do usuário dois números reais, e uma das 4 operações da matemática informadas pelo usuário, e faça o cálculo correspondente.
"""
# NOTE - O programa só se encerrará caso o usuário informe isso no programa.

while True:
    try:
        print(f"{'-'*20} CALCULADORA {'-'*20}\n")
        print("0 - Sair do programa")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")

        operador = input("Operação desejada: ").strip()

        match operador:
            case "0":
                print("Programa encerrado.")
                break
            case "1":
                x = float(input("Informe o valor de X: ").replace(",", "."))
                y = float(input("Informe o valor de Y: ").replace(",", "."))
                result = x+y

                print(f"A soma é {result}.")

                continue
            case "2":
                x = float(input("Informe o valor de X: ").replace(",", "."))
                y = float(input("Informe o valor de Y: ").replace(",", "."))
                result = x-y

                print(f"A subtração é {result}.")

                continue
            case "3":
                x = float(input("Informe o valor de X: ").replace(",", "."))
                y = float(input("Informe o valor de Y: ").replace(",", "."))
                result = x*y

                print(f"A multiplicação é {result}.")

                continue
            case "4":
                x = float(input("Informe o valor de X: ").replace(",", "."))
                y = float(input("Informe o valor de Y: ").replace(",", "."))
                result = x/y

                print(f"A divisão é {result}.")

                continue
            case _:
                print("Operação inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível calcular. {e}.")
        continue