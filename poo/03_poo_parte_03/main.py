# classe
class Pessoa:
    # método construtor
    def __init__(self, nome, idade, email, profissao): # type: ignore
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissao = profissao
    
    # método de ação
    def apresentar(self):
        print(f"Olá, eu meu chamo {self.nome}, tenho {self.idade} anos, trabalho como {self.profissao} e meu e-mail é {self.email}.")

# algoritmo principal
if __name__ == "__main__":
    # instancia a classe
    usuario = Pessoa("", 0, "", "")

    # tratamento de exceção
    try:
        # seta valores aos atributos do objeto
        usuario.nome = input("Informe o nome do usuário: ").title().strip()
        usuario.idade = int(input("Informe a idade: "))
        usuario.email = input("Informe o e-mail: ").lower().strip()
        usuario.profissao = input("Informe sua profissão: ").strip()

        # executa o método
        usuario.apresentar()
    except Exception as e:
        print(f"Não foi possível executar o programa. {e}.")