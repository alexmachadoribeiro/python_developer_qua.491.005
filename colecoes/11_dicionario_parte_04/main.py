# dicionário
usuario = { # type: ignore
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com",
    'profissão': "Programador"
}

# usuário informa qual chave ele irá deletar
chave = input("Informe o nome da chave que deseja deletar: ").lower().strip()

# tratamento de exceção
try:
    if chave in usuario:
        del usuario[chave]
        print("Chave excluída com sucesso!")
    else:
        print("Não foi possível achar a chave.")
except Exception as e:
    print(f"Não foi possível deletar a chave. {e}.")
finally:
    # exibe os valores do dicionário
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}.") # type: ignore