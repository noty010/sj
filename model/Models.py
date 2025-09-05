from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Time, Boolean, DECIMAL, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Evento(Base):
    __tablename__ = 'evento'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    handle = Column(String(255), unique=True, nullable=False)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    dia = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    endereco = Column(String(500), nullable=False)
    latitude = Column(DECIMAL(8, 5), nullable=False)
    longitude = Column(DECIMAL(8, 5), nullable=False)
    urlimagem = Column(String(255), nullable=False)


class Polo(Base):
    __tablename__ = 'polo'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    handle = Column(String(255), unique=True, nullable=False)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    inicio = Column(Date, nullable=False)
    fim = Column(Date, nullable=False)
    endereco = Column(String(500))
    latitude = Column(DECIMAL(8, 5))
    longitude = Column(DECIMAL(8, 5))
    ismultilocal = Column(Boolean, nullable=False, default=False)
    urlimagem = Column(String(255), nullable=False)
    
    # Relationships
    exibicoes = relationship('Exibicao', back_populates='polo')
    
    __table_args__ = (
        CheckConstraint(
            '(ismultilocal = 0 AND endereco IS NOT NULL AND latitude IS NOT NULL AND longitude IS NOT NULL) OR '
            '(ismultilocal = 1 AND endereco IS NULL AND latitude IS NULL AND longitude IS NULL)',
            name='chk_endereco_required'
        ),
        CheckConstraint('fim > inicio', name='chk_data'),
    )


class Exibicao(Base):
    __tablename__ = 'exibicao'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    ordem = Column(Integer)  # TINYINT UNSIGNED in SQLAlchemy is just Integer
    fkpolo = Column(Integer, ForeignKey('polo.code'), nullable=False)
    dia = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    endereco = Column(String(500), nullable=False)
    latitude = Column(DECIMAL(8, 5), nullable=False)
    longitude = Column(DECIMAL(8, 5), nullable=False)
    
    # Relationships
    polo = relationship('Polo', back_populates='exibicoes')
    atracoes = relationship('Atracao', back_populates='exibicao')


class Atracao(Base):
    __tablename__ = 'atracao'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    ordem = Column(Integer)  # TINYINT UNSIGNED in SQLAlchemy is just Integer
    fkexibicao = Column(Integer, ForeignKey('exibicao.code'), nullable=False)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    principal = Column(Boolean, nullable=False, default=False)
    urlimagem = Column(String(255), nullable=False)
    
    # Relationships
    exibicao = relationship('Exibicao', back_populates='atracoes')
    tags = relationship('Tag', secondary='atracaotags', back_populates='atracoes')


class Locais(Base):
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
    urlimage = Column(Text, nullable=False)
    urlicone = Column(String(255), nullable=False)
    
    # Relationships
    tags = relationship('Tag', secondary='locaistags', back_populates='locais')
    
    __table_args__ = (
        CheckConstraint('fim > inicio', name='chk_data'),
    )


class Pessoa(Base):
    __tablename__ = 'pessoa'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    handle = Column(String(255), unique=True, nullable=False)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    obras = Column(String(500), nullable=False)
    nascido = Column(Integer, nullable=False)
    morte = Column(Integer)
    ishomenageado = Column(Boolean, nullable=False, default=False)
    anohomenagem = Column(Integer)
    urlimagem = Column(String(255), nullable=False)
    
    __table_args__ = (
        CheckConstraint('morte > nascido', name='chk_data'),
    )


class Tag(Base):
    __tablename__ = 'tag'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    handle = Column(String(255), unique=True, nullable=False)
    nome = Column(String(255), nullable=False)
    
    # Relationships
    locais = relationship('Locais', secondary='locaistags', back_populates='tags')
    atracoes = relationship('Atracao', secondary='atracaotags', back_populates='tags')


class LocaisTags(Base):
    __tablename__ = 'locaistags'
    
    fklocal = Column(Integer, ForeignKey('locais.code'), primary_key=True)
    fktag = Column(Integer, ForeignKey('tag.code'), primary_key=True)


class AtracaoTags(Base):
    __tablename__ = 'atracaotags'
    
    fkatracao = Column(Integer, ForeignKey('atracao.code'), primary_key=True)
    fktag = Column(Integer, ForeignKey('tag.code'), primary_key=True)


class Usuario(Base):
    __tablename__ = 'usuario'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    isadmin = Column(Boolean, nullable=False, default=False)


class Equipe(Base):
    __tablename__ = 'equipe'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    funcao = Column(String(255), nullable=False)
    turma = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    ano = Column(String(50), nullable=False)
    urlimagem = Column(String(255))

url = "mysql+pymysql://root:aluno@localhost:3306/tccsj"
engine = create_engine (
    url,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600
)
Base.metadata.create_all(bind=engine)