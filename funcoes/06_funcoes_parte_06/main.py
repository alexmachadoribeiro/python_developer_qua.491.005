# bibliotecas
import os
import equacoes as eq

# algoritmo principal
if __name__ == "__main__":
    while True:
        try:
            print("1 - Calcular equação do 1º grau.")
            print("2 - Calcular equação do 2º grau.")
            print("3 - Sair do programa.")
            opcao = input("Informe a operação desejada: ").strip()

            os.system("cls" if os.name == "nt" else "clear")
            match opcao:
                case "1":
                    a = float(input("Informe o valor de 'a': ").replace(",", "."))
                    b = float(input("Informe o valor de 'b': ").replace(",", "."))
                    os.system("cls" if os.name == "nt" else "clear")
                    result = eq.equacao_1o_grau(a, b) # type: ignore
                    print(f"{a}x+{b} = 0" if b >= 0 else f"{a}x{b} = 0")
                    print(f"x = {result}")
                    continue
                case "2":
                    a = float(input("Informe o valor de 'a': ").replace(",", "."))
                    b = float(input("Informe o valor de 'b': ").replace(",", "."))
                    c = float(input("Informe o valor de 'c': ").replace(",", "."))
                    os.system("cls" if os.name == "nt" else "clear")
                    result = eq.equacao_2o_grau(a, b, c) # type: ignore
                    for x in result:
                        print(x)
                    continue
                case "3":
                    print("Programa encerrado.")
                    break
                case _:
                    print("Operação inválida.")
                    continue
        except Exception as e:
            print(f"Não foi possível calcular. {e}.")
            continue