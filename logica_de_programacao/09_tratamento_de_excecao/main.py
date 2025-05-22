# tratamento de exceção
try:
    # declaração de variável
    numero = int(input("Informe um número inteiro: "))

    # saída de dados
    print(f"O número informado é {numero}.")
except Exception as e:
    print(f"Não foi possível imprimir o número. {e}.")
finally:
    print("Programa encerrado.")