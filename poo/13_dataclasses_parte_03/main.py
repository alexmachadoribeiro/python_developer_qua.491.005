from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(nome="", profissao="", genero="", 
                           email="", telefone="", endereco="")
    empresa = PessoaJuridica(nome_fantasia="", cnpj="", website="",
                             email="", telefone="", endereco="")
    
    limpar()

    print(f"{'-'*20}Dados do usuário{'-'*20}")
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.profissao = input("Informe a profissão do usuário: ").strip()
    usuario.genero = input("Informe o gênero do usuário: ").strip()
    usuario.email = input("Informe o e-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()
    usuario.endereco = input("Informe o endereço do usuário: ").strip().title()

    print(f"{'-'*20}Dados da empresa{'-'*20}")
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNJ da empresa: ").strip()
    empresa.website = input("Informe o website da empresa: ").strip().lower()
    empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()

    limpar()

    # saída de dados
    print(f"{usuario}. Segue meus dados:")
    usuario.exibir_dados()
    print(f"{empresa}. Segue os dados da empresa:")
    empresa.exibir_dados()

    # destrói os objetos
    del(usuario)
    del(empresa)