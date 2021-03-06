from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime
from ..extensions.database import Base


class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True, autoincrement=True)
    comprador = Column(String(50), nullable=False)
    descricao = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    endereco = Column(String(100), nullable=False)
    fornecedor = Column(String(50), nullable=False)
    preco_unitario = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    create_at = Column(DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return f"Sale(id={self.id}, comprador={self.comprador}, descricao={self.descricao}, quantidade={self.quantidade}, endereco={self.quantidade}, fornecedor={self.fornecedor}, preco_unitario={self.preco_unitario}, create_at={self.create_at})"