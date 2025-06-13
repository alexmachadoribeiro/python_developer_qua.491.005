# dicionário
pessoa = { # type: ignore
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'cpf': "666.666.666-66"
}

# exibe os dados do dicionário
for dado in pessoa:
    print(f"{dado.capitalize()}: {pessoa.get(dado)}") # type: ignore