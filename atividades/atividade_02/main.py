"""
Crie um programa que receba o nome do usuário e a idade, e informe o menu abaixo:
Sala 1 - A Roda Quadrada - Livre
Sala 2 - A Volta dos Que Não Foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As Tranças do Rei Careca - 16 anos
Sala 5 - A Vingança do Farngo Assado - 18 anos
O usuário deverá escolher a sala do filme que deseja assistir, e o programa deverá:
- Liberar a entrada do usuário e encerrar, caso o usuário tenha a idade mínima, ou maior.
- Bloquear a entrada do usuário e pedir para o mesmo escolher outro filme, caso não tenha a idade mínima.
"""

try:
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    sala1 = "A Roda Quadrada"
    sala2 = "A Volta dos Que Não Foram"
    sala3 = "Poeira em Alto Mar"
    sala4 = "As Tranças do Rei Careca"
    sala5 = "A Vingança do Frango Assado"

    while True:
        print(f"{'-'*20} CINE COBRA {'-'*20}\n")
        print(f"Sala 1 - {sala1} - Livre")
        print(f"Sala 2 - {sala2} - 12 anos")
        print(f"Sala 3 - {sala3} - 14 anos")
        print(f"Sala 4 - {sala4} - 16 anos")
        print(f"Sala 5 - {sala5} - 18 anos")

        sala = input("Informe a sala escolhida: ").strip()

        match sala:
            case "1":
                filme = sala1
                idade_minima = 0
            case "2":
                filme = sala2
                idade_minima = 12
            case "3":
                filme = sala3
                idade_minima = 14
            case "4":
                filme = sala4
                idade_minima = 16
            case "5":
                filme = sala5
                idade_minima = 18
            case _:
                print("Sala inexistente.")
                continue
        
        if idade >= idade_minima:
            print(f"Filme escolhido por {nome}: {filme}.")
            print("Tenha um bom filme.")
            break
        else:
            print(f"{nome} não tem a idade mínima para ver {filme}.")
            print("Favor escolher outro filme.")
            continue
except Exception as e:
    print(f"Não foi possível executar o programa. {e}.")