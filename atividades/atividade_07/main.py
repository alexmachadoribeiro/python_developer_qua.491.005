# bibliotecas
import os

# lista
usuarios = []

# loop
while True:
    # menu
    print(f"{'-'*20} MENU {'-'*20}\n")
    print("1 - Inserir dados do novo usuário")
    print("2 - Exibir lista de usuários")
    print("3 - Alterar dados de um usuário já cadastrado")
    print("4 - Excluir usuário da lista")
    print("5 - Sair do programa")
    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            # inicializa o dicionário
            usuario = {}

            # input do usuário
            usuario['nome'] = input("Informe o nome: ").title().strip()
            usuario['data de nascimento'] = input("Data de nascimento: ").strip()
            usuario['email'] = input("Informe o e-mail: ").strip()
            usuario['cpf'] = input("Informe o CPF: ").strip()
            usuario['telefone'] = input("Informe o telefone: ").strip()
            usuario['profissão'] = input("Informe a profissão: ").strip()
            usuario['genero'] = input("Informe o gênero: ").strip()

            os.system("cls" if os.name == "nt" else "clear")
            try:
                # inserir os dados do dicionário na lista
                usuarios.append(usuario) # type: ignore
                print("Usuário cadastrado com sucesso.")
            except Exception as e:
                print(f"Não foi possível inserir novo usuário. {e}.")
            finally:
                continue
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("\nLista de usuários:")
            for i in range(len(usuarios)): # type: ignore
                print(f"{'-'*40}\n")
                print(f"Índice: {i}.")
                for chave in usuarios[i]: # type: ignore
                    print(f"{chave.capitalize()}: {usuarios[i].get(chave)}.") # type: ignore
            continue
        case "3":
            try:
                i = int(input("Informe o índice desejado: "))
                if i >= 0 and i < len(usuarios): # type: ignore
                    for chave in usuarios[i]: # type: ignore
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}") # type: ignore
                    chave_escolhida = input("Informe a chave que deseja alterar:").lower().strip()
                    usuarios[i][chave_escolhida] = input("Informe o novo valor: ").strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Chave alterada com sucesso.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar os dados. {e}.")
            finally:
                continue
        case "4":
            try:
                i = int(input("Informe o índice: "))
                if i >= 0 and i < len(usuarios): # type: ignore
                    for chave in usuarios[i]: # type: ignore
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}") # type: ignore
                    confirma = input("Tem certeza de que deseja excluir este usuário? (s/n) ").lower().strip()
                    match confirma: # type: ignore
                        case "s":
                            del(usuarios[i])
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuário deletado com sucesso.")
                        case "n":
                            os.system("cls" if os.name == "nt" else "clear")
                        case _:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Opção inválida. Operação cancelada.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível excluir usuário. {e}.")
            finally:
                continue
        case "5":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue

"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Inserir dados de novo usuário
- Exibir lista de usuários
- Alterar dados de um usuário já cadastrado
- Excluir usuário da lista
- Sair do programa
Os dados a serem cadastrados serão os seguintes:
- Nome
- Data de Nascimento
- E-mail
- CPF
- Telefone
- Profissão
- Gênero
# NOTE - a lista deve começar vazia
"""