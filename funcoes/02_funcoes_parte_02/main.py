# função
def dar_boas_vindas(nome): # type: ignore
    print(f"Seja bem vindo {nome}.")

# algoritmo principal
nome = input("Informe seu nome: ")
dar_boas_vindas(nome)