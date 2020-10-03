# Projeto Teach.me

Sistema Web para busca de professores particulares voltada à alunos universitários desenvolvido conjuntamente para as disciplinas de **SCC0219 - Introdução ao Desenvolvimento Web** e **SCC0240 - Bases de Dados**.

## Objetivo do projeto

O projeto teve como objetivo a criação e implementação de um sistema a fim de tanto aplicar os conhecimentos adquiridos quantos às tecnologias utilizadas na web quanto modelar e projetar a base de dados necessária para que a aplicação funcionasse. O documento final demonstrando todas as etapas para o projeto da base de dados se encontra no arquivo PDF da raíz.

## Tecnologias utilizadas

- **PostgreSQL v10.12** - SGBD Relacional
- **ReactJS + NPM**     - Aplicação Front-end
- **Django**            - API

## Estrutura de Arquivos 

```
readme.md        - Informações Gerais do projeto
/database        - Arquivos referentes à implementação da base de dados
| -- setup.sql   - Arquivo para criar a base e configurar seu usuário
| -- teachme_db.sql - SQL com o script de criação das tabelas
| -- mockup_data.sql - Script para popular as tabelas
| -- queries.sql  - Consultas de dificuldade média criadas para o projeto
| -- conn_test.py - Script para testar a conexão do python com a base
/api              - Protótipo de API criada com Django
/teachme-app      - Protótipo de interface em React que consome a API
```

## Autores do Projeto
Alberto Neves
Gabriel Van Loon
Tamiris Tinelli
