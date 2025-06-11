# declaração de lista
carrinho = []

while True:
    item = input("Informe o item: ").capitalize().strip()
    carrinho.append(item) # type: ignore
    print(f"{item} inserido no carrinho com sucesso!")
    confirmar = input("Deseja inserir outro item? (s/n)").lower().strip()
    match confirmar:
        case "s":
            continue
        case "n":
            break
        case _:
            print("Opção inválida.")
            continue

# ordena a lista em ordem alfabética
carrinho.sort() # type: ignore

# exibe os itens da lista
for item in carrinho: # type: ignore
    print(item) # type: ignore