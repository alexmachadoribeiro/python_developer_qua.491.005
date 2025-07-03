from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

try:
    engine = create_engine("sqlite:///meu_primeiro_banco.db")
    Base = declarative_base()

    # cria a entidade pessoa
    class Pessoa(Base):
        # nome da entidade
        __tablename__ = "pessoa"

        # atributos
        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        # FIXME - data_nasc = Column(Date, nullable=False)
        email = Column(String, nullable=False, unique=True)
        cpf = Column(String, nullable=False, unique=True)
        genero = Column(String, nullable=True)
        tipo_sanguineo = Column(String, nullable=True)
    
    # cria a tabela
    Base.metadata.create_all(engine)

    # msg
    print("Entidade Pessoa criada com sucesso.")
except Exception as e:
    print(f"Erro no sistema. {e}.")

try:
    Session = sessionmaker(bind=engine)
    session = Session()

    # cadastrar usuário no banco
    nome = input("Informe o nome: ").strip().title()
    # FIXME - data_nasc = input("Informe a data de nascimento: (aaaa-mm-dd): ").strip()
    email = input("Informe o e-mail: ").strip().lower()
    cpf = input("Informe o CPF: ").strip()
    genero = input("Informe o gênero: ").strip()
    tipo_sanguineo = input("Informe o tipo sanguíneo: ").strip().upper()

    nova_pessoa = Pessoa(
        nome=nome,
        # FIXME - data_nasc=data_nasc,
        email=email,
        cpf=cpf,
        genero=genero,
        tipo_sanguineo=tipo_sanguineo
    )

    session.add(nova_pessoa)
    session.commit()

    print("Pessoa cadastrada com sucesso.")

    session.close()
except Exception as e:
    print(f"Não foi possível cadastrar novo usuário. {e}.")