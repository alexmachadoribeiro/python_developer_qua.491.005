from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

try:
    engine = create_engine("mysql+mysqlconnector://root:@localhost:3308/teste")
    Base = declarative_base()

    class Usuario(Base):
        __tablename__ = "usuario"

        id_usuario = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(255), nullable=False)
        email = Column(String(255), nullable=False, unique=True)

    # cria a tabela
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Erro ao criar a tabela: {e}")