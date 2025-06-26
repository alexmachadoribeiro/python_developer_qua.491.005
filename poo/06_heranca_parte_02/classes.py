# superclasses
class Pai:
    def __init__(self, genero, peso, altura):
        self.genero = genero
        self.peso = peso
        self.altura = altura
    
    def exibir_info(self):
        print(f"Gênero: {self.genero}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")

class Mae:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")

# subclasse
class Filho(Pai, Mae):
    def __init__(self, nome, email, telefone, genero, peso, altura):
        Mae.__init__(self, nome, email, telefone)
        Pai.__init__(self, genero, peso, altura)
    
    def exibir_info(self):
        Mae.exibir_info(self)
        Pai.exibir_info(self)