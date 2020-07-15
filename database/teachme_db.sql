-- Script:      teachme_db.sql
-- Descrição:   Script contendo os comandos SQL para a criação das tabelas 
--              do banco de dados Postgresql do projeto Teach.me
-- Data:        10/06/2020 
-- Versão:      1.0.0

CREATE TABLE usuario(                                   -- Estrutura: OK, Normalização: TODO
    NOME_USUARIO  VARCHAR(30),
    EMAIL         VARCHAR(60) NOT NULL, 
    SENHA         VARCHAR(400) NOT NULL,
    NOME          VARCHAR(60) NOT NULL,
    SOBRENOME     VARCHAR(60),
    FOTO          VARCHAR(100),
    E_INSTRUTOR   BOOLEAN,

    CONSTRAINT PK_USUARIO PRIMARY KEY(NOME_USUARIO),
    CONSTRAINT SK_USUARIO UNIQUE (EMAIL)
);
    
CREATE TABLE instrutor(                                 -- Estrutura: OK, Normalização: TODO
    NOME_USUARIO  VARCHAR(30),
    RESUMO        VARCHAR(300),
    SOBRE_MIM     VARCHAR(3000),
    FORMACAO      VARCHAR(100),

    CONSTRAINT PK_INSTRUTOR         PRIMARY KEY (NOME_USUARIO),
    CONSTRAINT FK_INSTRUTOR_USUARIO FOREIGN KEY(NOME_USUARIO) 
        REFERENCES usuario(NOME_USUARIO) 
        ON DELETE CASCADE
);
    
CREATE TABLE turma(                                     -- Estrutura: OK, Normalização: TODO
    NOME              VARCHAR(30),
    TITULO            VARCHAR(60) NOT NULL,
    DESCRICAO         VARCHAR(300),
    IMAGEM            VARCHAR(100),
    QTD_PARTICIPANTES SMALLINT,
    MAX_PARTICIPANTES SMALLINT    NOT NULL,
    SITUACAO          VARCHAR(10),

    CONSTRAINT PK_TURMA PRIMARY KEY (NOME)              -- @TODO: Se quiser fazer o CHECK qtd <= max pode
                                                        -- @TODO: Se quiser fazer max >= 0 e qtd >= pode tbm
);
    
CREATE TABLE participante(                              -- Estrutura: OK, Normalização: TODO
    ALUNO   VARCHAR(30),
    TURMA   VARCHAR(30),
    E_LIDER BOOLEAN,

    CONSTRAINT PK_PARTICIPANTE          PRIMARY KEY(ALUNO, TURMA),
    CONSTRAINT FK_PARTICIPANTE_USUARIO  FOREIGN KEY (ALUNO) 
        REFERENCES usuario(NOME_USUARIO)    
        ON DELETE CASCADE,
    CONSTRAINT FK_PARTICIPANTE_TURMA    FOREIGN KEY (TURMA) 
        REFERENCES turma(NOME) 
        ON DELETE CASCADE
);

CREATE TABLE recomenda(                                 -- Estrutura: OK, Normalização: TODO
    ALUNO     VARCHAR(30),
    INSTRUTOR VARCHAR(30),
    TEXTO     VARCHAR(300),

    CONSTRAINT PK_RECOMENDA         PRIMARY KEY(ALUNO, INSTRUTOR),
    CONSTRAINT FK_RECOMENDA_USUARIO FOREIGN KEY (ALUNO) 
        REFERENCES usuario(NOME_USUARIO) 
        ON DELETE CASCADE,
    CONSTRAINT FK_RECOMENDA_INSTRUTOR FOREIGN KEY (INSTRUTOR) 
        REFERENCES instrutor(NOME_USUARIO) 
        ON DELETE CASCADE
    );

CREATE TABLE disciplina(                                -- Estrutura: OK, Normalização: TODO
    NOME            VARCHAR(30),
    DISCIPLINA_PAI  VARCHAR(30),
    
    CONSTRAINT PK_DISCIPLINA PRIMARY KEY(NOME)
    CONSTRAINT FK_DISCIPLINA_DISCIPLINA FOREIGN KEY (DISCIPLINA)
        REFERENCES disciplina(NOME)
        ON DELETE SET NULL
);


CREATE TABLE oferecimento(                              -- Estrutura: @TODO, Normalização: TODO
    INSTRUTOR   VARCHAR(30),
    DISCIPLINA  VARCHAR(30),                    
    PRECO_BASE  REAL NOT NULL,                          -- @TODO: Real é de precisão flutuante, arrumar
    METODOLOGIA VARCHAR(100),
    
    CONSTRAINT PK_OFERECIMENTO            PRIMARY KEY (INSTRUTOR, DISCIPLINA),
    CONSTRAINT FK_OFERECIMENTO_INSTRUTOR  FOREIGN KEY (INSTRUTOR) 
        REFERENCES instrutor(NOME_USUARIO) 
        ON DELETE CASCADE,
    CONSTRAINT FK_OFERECIMENTO_DISCIPLINA FOREIGN KEY (DISCIPLINA) 
        REFERENCES disciplina(NOME) 
        ON DELETE CASCADE,
    CONSTRAINT CK_PRECO_OFERECIMENTO      CHECK (PRECO_BASE >= 0)
);

CREATE TABLE proposta(                                  -- Estrutura: @TODO, Normalização: TODO
    ID            BIGSERIAL,                            -- @TODO: https://www.postgresqltutorial.com/postgresql-uuid/
    TURMA         VARCHAR(30) NOT NULL,
    INSTRUTOR     VARCHAR(30) NOT NULL,
    DISCIPLINA    VARCHAR(30) NOT NULL,
    CODIGO        BIGSERIAL   NOT NULL,                 -- @TODO: O código tem que ser no máximo 3 caracteres pra ser user friendly
    STATUS        VARCHAR(10) NOT NULL,
    DATA_CRIACAO  TIMESTAMP   NOT NULL,
    PRECO_TOTAL   REAL        NOT NULL,                 -- @TODO: Real é de precisão flutuante, arrumar

    CONSTRAINT PK_PROPOSTA              PRIMARY KEY (ID),
    CONSTRAINT SK_PROPOSTA              UNIQUE(TURMA, INSTRUTOR, DISCIPLINA, CODIGO), --SECONDARY KEY (SK)
    CONSTRAINT FK_PROPOSTA_TURMA        FOREIGN KEY (TURMA) 
        REFERENCES turma(NOME) 
        ON DELETE CASCADE,
    CONSTRAINT FK_PROPOSTA_OFERECIMENTO FOREIGN KEY(INSTRUTOR, DISCIPLINA) 
        REFERENCES oferecimento(INSTRUTOR, DISCIPLINA) 
        ON DELETE CASCADE,
    CONSTRAINT CK_PRECO_PROPOSTA        CHECK (PRECO_TOTAL >= 0)
);

CREATE TABLE aceita(                        -- Estrutura: @TODO, Normalização: TODO 
    ALUNO     VARCHAR(30),
    TURMA     VARCHAR(30),
    PROPOSTA  BIGSERIAL,                    -- @TODO: https://www.postgresqltutorial.com/postgresql-uuid/

    CONSTRAINT PK_ACEITA              PRIMARY KEY(ALUNO, TURMA, PROPOSTA),
    CONSTRAINT FK_ACEITA_PARTICIPANTE FOREIGN KEY (ALUNO, TURMA) 
        REFERENCES participante (ALUNO, TURMA),
    CONSTRAINT FK_ACEITA_PROPOSTA     FOREIGN KEY (PROPOSTA) 
        REFERENCES proposta(ID)
);

CREATE TABLE local(                         -- Estrutura: OK, Normalização: TODO 
    INSTRUTOR   VARCHAR(30),
    NOME        VARCHAR (100),
    CAPACIDADE  SMALLINT      NOT NULL,
    RUA         VARCHAR(100)  NOT NULL,
    NUMERO      SMALLINT      NOT NULL,
    BAIRRO      VARCHAR(100)  NOT NULL,     
    COMPLEMENTO VARCHAR(100),
    CIDADE      VARCHAR(30)   NOT NULL,
    UF          VARCHAR(2)    NOT NULL,

    CONSTRAINT PK_LOCAL             PRIMARY KEY (INSTRUTOR, NOME),
    CONSTRAINT FK_LOCAL_INSTRUTOR   FOREIGN KEY (INSTRUTOR) 
        REFERENCES instrutor(NOME_USUARIO) 
        ON DELETE CASCADE,
    CONSTRAINT CK_CAPACIDADE_LOCAL  CHECK (CAPACIDADE >= 0)
);

CREATE TABLE horario_disponivel(            -- Estrutura: OK Normalização: TODO 
    INSTRUTOR   VARCHAR(30),
    DIA_SEMANA  VARCHAR(10),
    HORARIO     TIME,
    CONSTRAINT PK_HORARIO           PRIMARY KEY (INSTRUTOR, DIA_SEMANA, HORARIO),
    CONSTRAINT FK_HORARIO_INSTRUTOR FOREIGN KEY (INSTRUTOR) 
        REFERENCES instrutor (NOME_USUARIO) 
        ON DELETE CASCADE                   
                                            -- @TODO: Se quiser dá pra fazer um check do tipo
                                            -- DIA_SEMANA in ('DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB')
);

CREATE TABLE aula(                              -- Estrutura: TODO, Normalização: TODO
    PROPOSTA        BIGSERIAL,                  -- @TODO: https://www.postgresqltutorial.com/postgresql-uuid/
    NUMERO          SMALLINT,                   -- @TODO: Não faz sentido ser BIGSERIAL, o cara vai marcar 1 trilhão de aulas? SMALLINT
    INSTRUTOR       VARCHAR(30) NOT NULL,
    LOCAL           VARCHAR(100),
    PRECO_FINAL     REAL        NOT NULL,       -- @TODO: Real é de precisão flutuante, arrumar
    STATUS          VARCHAR(10) NOT NULL,
    DATA_INICIO     TIMESTAMP   NOT NULL,
    DATA_FIM        TIMESTAMP   NOT NULL,
    NOTA_INSTRUTOR  SMALLINT,                   -- @TODO: Nota é valor inteiro de 0 À 5 (vide documentação)

    CONSTRAINT PK_AULA          PRIMARY KEY (PROPOSTA, NUMERO),
    CONSTRAINT FK_AULA_PROPOSTA FOREIGN KEY (PROPOSTA) 
        REFERENCES proposta(ID),
    CONSTRAINT FK_AULA_LOCAL    FOREIGN KEY (INSTRUTOR, LOCAL) 
        REFERENCES local(INSTRUTOR, NOME),
    CONSTRAINT CK_NOTA_VALIDA   CHECK (NOTA_INSTRUTOR >= 0 AND NOTA_INSTRUTOR <= 5)
);

CREATE TABLE avaliacao_participante(    -- Estrutura: TODO, Normalização: TODO
    ALUNO     VARCHAR(30),
    TURMA     VARCHAR(30),
    PROPOSTA  BIGSERIAL,                -- @TODO: https://www.postgresqltutorial.com/postgresql-uuid/
    NUMERO    SMALLINT,
    NOTA      SMALLINT NOT NULL,

    CONSTRAINT PK_AVALIACAO               PRIMARY KEY (ALUNO, TURMA, PROPOSTA, NUMERO),
    CONSTRAINT FK_AVALIACAO_PARTICIPANTE  FOREIGN KEY (ALUNO, TURMA) 
        REFERENCES participante(ALUNO, TURMA),
    CONSTRAINT FK_AVALIACAO_AULA          FOREIGN KEY (PROPOSTA, NUMERO) 
        REFERENCES aula (PROPOSTA, NUMERO)
);

CREATE TABLE chat (                     -- Estrutura: TODO, Normalização: TODO
    TURMA     VARCHAR(30),
    CODIGO    BIGSERIAL,                -- @TODO: https://www.postgresqltutorial.com/postgresql-uuid/
    NOME      VARCHAR(30) NOT NULL,
    STATUS    VARCHAR(10) NOT NULL,
    INSTRUTOR VARCHAR(30),

    CONSTRAINT PK_CHAT           PRIMARY KEY (TURMA, CODIGO),
    CONSTRAINT FK_CHAT_TURMA     FOREIGN KEY (TURMA) 
        REFERENCES turma (NOME) 
        ON DELETE CASCADE,
    CONSTRAINT FK_CHAT_INSTRUTOR FOREIGN KEY (INSTRUTOR) 
        REFERENCES instrutor (NOME_USUARIO) 
        ON DELETE CASCADE
);

CREATE TABLE mensagem(                  -- Estrutura: TODO, Normalização: TODO
    TURMA     VARCHAR(30),
    CODIGO    BIGSERIAL,                -- @TODO: https://www.postgresqltutorial.com/postgresql-uuid/
    NUMERO    INTEGER,                  -- @TODO: Verificar se existe AUTO INCREMENT em chave composta
    USUARIO   VARCHAR(30),
    DATA_ENVIO TIMESTAMP NOT NULL,
    CONTEUDO  VARCHAR(140),

    CONSTRAINT PK_MENSAGEM          PRIMARY KEY (TURMA, CODIGO, NUMERO),
    CONSTRAINT FK_MENSAGEM_CHAT     FOREIGN KEY (TURMA, CODIGO)
        REFERENCES CHAT (TURMA, CODIGO) 
        ON DELETE CASCADE,
    CONSTRAINT FK_MENSAGEM_USUARIO  FOREIGN KEY (USUARIO)
        REFERENCES usuario (NOME_USUARIO) 
        ON DELETE SET NULL
);
