from dataclasses import dataclass
from abc import ABC
from abc import abstractmethod

@dataclass
class Pessoa(ABC):
    email: str
    telefone: str
    endereco: str

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

@dataclass
class PessoaFisica(Pessoa):
    nome: str
    profissao: str
    genero: str

    def __str__(self):
        return f"Olá, eu sou {self.nome}, gênero {self.genero}, trabalho como {self.profissao}, meu e-mail é {self.email}, meu telefone é {self.telefone} e moro no endereço {self.endereco}."
    
    def __len__(self):
        pass

    def __del__(self):
        print(f"Objeto {self.nome} destruído com sucesso.")
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Profissão: {self.profissao}")
        print(f"Gênero: {self.genero}")
        super().exibir_dados()

@dataclass
class PessoaJuridica(Pessoa):
    nome_fantasia: str
    cnpj: str
    website: str

    def __str__(self):
        return f"Somos da empresa {self.nome_fantasia}, com CNPJ {self.cnpj}. Nosso website é {self.website}, nosso e-mail é {self.email}, nosso telefone é {self.telefone}, e nosso endereço é {self.endereco}."
    
    def __len__(self):
        pass

    def __del__(self):
        print(f"Objeto {self.nome_fantasia} destruído com sucesso.")
    
    def exibir_dados(self):
        print(f"Nome da empresa: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Website: {self.website}")
        super().exibir_dados()