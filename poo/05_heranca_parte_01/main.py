# bibliotecas
import os
import classes

# algoritmo principal
if __name__ == "__main__":
    # instancia de objetos
    usuario = classes.PessoaFisica("", "", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "", "")

    # limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

    # atribui valores ao objeto do tipo Pessoa Física
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}\n")

    usuario.nome = input("Informe seu nome: ").title().strip()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.profissao = input("Informe sua profissão: ").strip()
    usuario.genero = input("Informe seu gênero: ").strip()
    usuario.email = input("Informe seu e-mail: ").strip().lower()
    usuario.endereco = input("Informe seu endereço: ").strip().title()
    usuario.telefone = input("Informe seu telefone: ").strip()

    # limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

    # atribui valores ao objeto do tipo Pessoa Jurídica
    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}\n")

    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
    empresa.nome_fantasia = input("Informe o nome fantasia: ").title().strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    # limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

    # exibe os dados do usuário e da empresa
    print("Dados do usuário:\n")
    usuario.exibir_dados()
    print("-"*60)
    print("Dados da empresa:\n")
    empresa.exibir_dados()