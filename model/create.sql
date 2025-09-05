USE tccsj;

-- Tabela de Eventos como Comidas Gigantes, Queermesse, etc.
DROP TABLE IF EXISTS evento;
CREATE TABLE evento(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    id VARCHAR(255) UNIQUE NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    dia DATE NOT NULL,
    horario TIME NOT NULL,
    endereco VARCHAR(500) NOT NULL,
    latitude DECIMAL(8,5) NOT NULL,
    longitude DECIMAL(8,5) NOT NULL
);

-- Tabela de Polos como Pátio do Forró, Azulão, SJ na Roça, etc.
DROP TABLE IF EXISTS polo;
CREATE TABLE polo(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    id VARCHAR(255) UNIQUE NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    inicio DATE NOT NULL,
    fim DATE NOT NULL,
    endereco VARCHAR(500),
    latitude DECIMAL(8,5),
    longitude DECIMAL(8,5),
    ismultilocal BOOLEAN NOT NULL DEFAULT 0,

    CONSTRAINT chk_endereco_required CHECK ( --Checa se o polo é multilocal ou não e exige os campos de endereço e coordenadas se não for
        (ismultilocal = 0 AND endereco IS NOT NULL AND latitude IS NOT NULL AND longitude IS NOT NULL
        ) OR (
            ismultilocal = 1 AND endereco IS NULL AND latitude IS NULL AND longitude IS NULL
        )
    ),

    CONSTRAINT chk_data CHECK (
        fim > inicio
    )
);

-- Tabela de exibições em determinado polo
DROP TABLE IF EXISTS exibicao;
CREATE TABLE exibicao(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    ordem TINYINT UNSIGNED,
    fkpolo INT NOT NULL,
    dia DATE NOT NULL,
    horario TIME NOT NULL,
    endereco VARCHAR(500) NOT NULL,
    latitude DECIMAL(8,5) NOT NULL,
    longitude DECIMAL(8,5) NOT NULL,
    FOREIGN KEY (fkpolo) REFERENCES polo(cod)
);

-- Tabela de Atrações em determinada exibição de um polo
DROP TABLE IF EXISTS atracao;
CREATE TABLE atracao(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    ordem TINYINT UNSIGNED,
    fkexibicao INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    principal BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (fkexibicao) REFERENCES exibicao(cod)
);

-- Tabela de Locais de Interesse
DROP TABLE IF EXISTS locais;
CREATE TABLE locais(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    id VARCHAR(255) UNIQUE NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    dias VARCHAR(255),
    inicio TIME NOT NULL,
    fim TIME NOT NULL,
    endereco VARCHAR(500) NOT NULL,
    latitude DECIMAL(8,5) NOT NULL,
    longitude DECIMAL(8,5) NOT NULL,
    urlimage TEXT NOT NULL,
    urlicone VARCHAR(255) NOT NULL

    CONSTRAINT chk_data (
        fim > inicio
    )
);

-- Personalidades marcantes ou homenageados
DROP TABLE IF EXISTS pessoa;
CREATE TABLE pessoa(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    id VARCHAR(255) UNIQUE NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    obras VARCHAR(500) NOT NULL,
    nascido INT NOT NULL,
    morte INT,
    ishomenageado BOOLEAN NOT NULL DEFAULT 0,
    anohomenagem INT,
    
    CONSTRAINT chk_data (
        morte > nascido
    )
);

-- Tabela de tags (Cultural, Comercio, etc)
DROP TABLE IF EXISTS tag;
CREATE TABLE tag(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    id VARCHAR(255) UNIQUE NOT NULL,
    nome VARCHAR(255) NOT NULL
);

-- Relacionamento n para n de Tags e Locais
DROP TABLE IF EXISTS locaistags;
CREATE TABLE locaistags(
    fklocal INT,
    fktag INT,
    PRIMARY KEY (fklocal, fktag),
    FOREIGN KEY (fklocal) REFERENCES locais(cod),
    FOREIGN KEY (fktag) REFERENCES tag(cod)
);

-- Relacionamento n para n de Atrações e Tags
DROP TABLE IF EXISTS atracaotags;
CREATE TABLE atracaotags(
    fkatracao INT,
    fktag INT,
    PRIMARY KEY (fkatracao, fktag),
    FOREIGN KEY (fkatracao) REFERENCES atracao(cod),
    FOREIGN KEY (fktag) REFERENCES tag(cod)
)

DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario(
    cod INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    isadmin BOOLEAN NOT NULL DEFAULT 0
);

DROP TABLE IF EXISTS equipe;
CREATE TABLE equipe (
	cod int primary key auto_increment,
    nome varchar(255) not null,
    funcao varchar(255) not null,
    turma varchar(255) not null,
    email varchar(255) not null,
    ano year not null,
    urlfoto varchar(255)
);
