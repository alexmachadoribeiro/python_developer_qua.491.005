# tratamento de exceção
try:
    # declaração de variável
    n = int(input("Informe um número inteiro positivo: "))

    # laço de repetição
    while n >= 0:
        print(n)
        n -= 1
except Exception as e:
    print(f"Não foi possível fazer a contagem. {e}.")
finally:
    print("Programa encerrado.")