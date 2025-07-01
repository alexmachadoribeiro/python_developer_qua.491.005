from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereco: str

@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str
    profissao: str
    
    def __str__(self):
        return f"Olá, meu nome é {self.nome}, trabalho como {self.profissao}, e meu CPF é {self.cpf}, meu e-mail é {self.email}, meu telefone é {self.telefone} e meu endereço é {self.endereco} e minha altura é {len(self)} metros."
    
    def __del__(self):
        print(f"Objeto {self.nome} destruído com sucesso.")

@dataclass
class PessoaJuridica(Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str

    def __str__(self):
        return f"Somos da empresa {self.nome_fantasia}, de razão social {self.razao_social}, nosso CNPJ é {self.cnpj}. Pode nos contactar pelo e-mail {self.email}, ou por telefone, {self.telefone}. Se preferir, vá ao nosso endereço {self.endereco}."
    
    def __del__(self):
        print(f"Objeto {self.nome_fantasia} destruído com sucesso.")