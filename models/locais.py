from sqlalchemy import Column, String, Text, Time, DECIMAL, CheckConstraint, Integer
from sqlalchemy.orm import relationship
from .base import BaseModel

class Locais(BaseModel):
    __tablename__ = 'locais'

    code = Column(Integer, primary_key=True, autoincrement=True)
    handle = Column(String(255), unique=True, nullable=False)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    dias = Column(String(255))
    inicio = Column(Time, nullable=False)
    fim = Column(Time, nullable=False)
    endereco = Column(String(500), nullable=False)
    latitude = Column(DECIMAL(8, 5), nullable=False)
    longitude = Column(DECIMAL(8, 5), nullable=False)
    urlimage = Column(String(255), nullable=False)
    urlicone = Column(String(255), nullable=False)

    tags = relationship('Tag', secondary='locaistags', back_populates='locais')
    __table_args__ = (
        CheckConstraint('fim > inicio', name = 'checkdata'),
    )