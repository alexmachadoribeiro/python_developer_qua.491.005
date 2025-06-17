chaves = ('Nome', 'Idade', 'E-mail', "Profissão")
pessoas = [ # type: ignore
    {
        chaves[0]: "Alex Machado",
        chaves[1]: 40,
        chaves[2]: "alex@gmail.com",
        chaves[3]: "CEO"
    },
    {
        chaves[0]: "Maria da Silva",
        chaves[1]: 25,
        chaves[2]: "maria@gmail.com",
        chaves[3]: "Assistente Administrativo"
    }
]

# inserindo novo dicionário
pessoa = {}

# inserindo dados no novo dicionário
try:
    for chave in chaves:
        if chave == "Idade":
            pessoa[chave] = int(input("Informe Idade: "))
        else:
            pessoa[chave] = input(f"Informe {chave}: ")
    pessoas.append(pessoa) # type: ignore
    print(f"{pessoa.get(chaves[0])} inserida com sucesso.") # type: ignore
except Exception as e:
    print(f"Não foi possível cadastrar nova pessoa. {e}.")
finally:
    for pessoa in pessoas: # type: ignore
        for chave in pessoa:
            print(f"{chave}: {pessoa.get(chave)}.") # type: ignore
        print(f"\n{'-'*40}\n")