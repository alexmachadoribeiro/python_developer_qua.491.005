# lista de dicionários
pessoas = [ # type: ignore
    {
        'nome': "Fulano",
        'idade': 18,
        'email': "fulano@gmail.com",
        'profissão': "Programador"
    },
    {
        'nome': "Cicrano",
        'idade': 25,
        'email': "cicrano@gmail.com",
        'profissão': "DBA"
    },
    {
        'nome': "Beltrano",
        'idade': 30,
        'email': "beltrano@gmail.com",
        'profissão': "Gerente de Projetos"
    }
]

# exibição dos dados dos dicionários da lista
# for pessoa in pessoas: # type: ignore
#     for chave in pessoa:
#         print(f"{chave.capitalize()}: {pessoa.get(chave)}.") # type: ignore
#     print(f"\n{'-'*40}\n")

# novo dicionário
nova_pessoa = { # type: ignore
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'profissão': "CEO"
}

# adicionando novo dicionário à lista
pessoas.append(nova_pessoa) # type: ignore

# exibe nova lista de dicionários
print(f"\nNOVA LISTA:\n")
for pessoa in pessoas: # type: ignore
    for chave in pessoa:
        print(f"{chave.capitalize()}: {pessoa.get(chave)}.") # type: ignore
    print(f"\n{'-'*40}\n")