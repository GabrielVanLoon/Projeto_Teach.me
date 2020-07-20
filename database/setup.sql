-- Script:      setup.sql
-- Descrição:   Script contendo os comandos SQL para a criação do banco de dados
--              e seus usuários.
-- Data:        10/06/2020 
-- Versão:      1.0.0

-- Se for fazer via terminal:
-- $ sudo -i -u postgres

-- CRIANDO A BASE DE DADOS
DROP DATABASE IF EXISTS teachme_db;
DROP USER IF EXISTS teachme_user;

CREATE DATABASE teachme_db
    WITH ENCODING 'UTF8';

-- CRIANDO O USUÁRIO E DEFININDO PRIVILÉGIOS
CREATE USER teachme_user WITH PASSWORD 'Th3Cl4ws0fW1nt3rSubV3RtTh3wEak';
GRANT ALL PRIVILEGES ON DATABASE teachme_db TO teachme_user;

-- Comando para testar se tá tudo ok: 
-- $ psql -d teachme_db -U teachme_user -W -h localhost