# dicionário
pessoa = {
    'nome': "Alex Machado",
    'email': "alex@gmail.com"
}

# exibe os dados
print(f"Nome: {pessoa['nome']}")
print(f"E-mail: {pessoa.get('email')}")

# exibe dados inexistentes
print(f"Idade: {pessoa.get('idade')}")

# inserindo a idade da pessoa
try:
    pessoa['idade'] = int(input("Informe a idade: ")) # type: ignore
except Exception as e:
    print(f"Não foi possível inserir o novo valor. {e}.")
finally:
    print(f"Nome: {pessoa.get('nome')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"Idade: {pessoa.get('idade')}")