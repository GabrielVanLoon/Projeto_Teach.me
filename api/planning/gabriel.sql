-- Selecionar nome_usuario, nome, nome da disciplina, preço base e metodologia dos instrutores que
-- realizam aulas em uma cidade, possuem disponibilidade no horário indicado e cujo valor base
-- da disciplina solicitada esteja dentro de um intervalo de preço pré-definido
-- [Fácil porém com bastante junções]
    SELECT U.NOME_USUARIO, U.NOME, OF.DISCIPLINA, OF.PRECO_BASE, OF.METODOLOGIA
        FROM oferecimento 'OF'
        INNER JOIN usuario 'U' ON (OF.INSTRUTOR = U.NOME_USUARIO)
        INNER JOIN local 'L' ON (U.NOME_USUARIO = OF.INSTRUTOR)
        INNER JOIN horario_disponivel 'HR' ON (U.NOME_USUARIO = HR.INSTRUTOR)
        WHERE  OF.DISCIPLINA = 'Cálculo' AND OF.PRECO_BASE > 0.00 AND OF.PRECO_BASE < 50.00
            AND L.CIDADE = 'São Carlos' AND L.UF = 'SP' 
            AND HR.DIA_SEMANA = 'SEG' AND HR.HORARIO = '14:30:00'

-- Selecionar, para cada turma existente na base de dados, a quantidade total de propostas
-- FINALIZADAS ou APROVADAS cujo preço total das aulas foi superior ou igual à R$ 100.00.
-- [Fácil]
    SELECT P.TURMA, COUNT() 'QUANTIDADE'
        FROM proposta 'P' 
        WHERE P.PRECO_TOTAL >= 100.00 AND (P.STATUS = 'FINALIZADA' OR P.STATUS = 'APROVADA')
        GROUP BY P.TURMA 

-- Retorne a quantide de horas que cada instrutor do sistema deu de aula nos últimos 30 dias    
-- [Fácil/Médio - Gabriel] Ref: http://www.sqlines.com/postgresql/how-to/datediff

    -- 1ª Versão 
    SELECT P.INSTRUTOR, SUM(D.DURACAO)
        FROM proposta 'P' 
        INNER JOIN 
            (SELECT A.PROPOSTA, DATE_PART('hour', A.DATA_INICIO - A.DATA_FIM) 'DURACAO'
                FROM aula 'A' 
                WHERE A.STATUS = 'FINALIZADA' 
                    AND A.DATA_INICIO >= ('now'::timestamp - '1 month'::interval)) as 'D'
            ON (P.ID = D.PROPOSTA)
        GROUP BY P.INSTRUTOR

    -- 2ª Versão
    SELECT P.INSTRUTOR, SUM(DATE_PART('hour', A.DATA_INICIO - A.DATA_FIM)) 'HORAS'
        FROM aula 'A' 
        INNER JOIN proposta 'P' ON (P.ID = A.PROPOSTA)
        WHERE A.STATUS = 'FINALIZADA' 
            AND A.DATA_INICIO >= ('now'::timestamp - '1 month'::interval)
        GROUP BY P.INSTRUTOR

-- Retornar o username e o score dos 10 instrutores com a maior média de avaliação na plataforma. 
-- Em caso de empate o desempate  deve ser feito pela quantidade de aulas dadas.
-- [Médio] 
    SELECT A.INSTRUTOR, AVG(AP.NOTA) 'SCORE', COUNT(DISTINCT ROW(A.PROPOSTA, A.NUMERO)) 'QTD'
        FROM aula 'A'
        INNER JOIN avaliacao_participante 'AP' ON (A.PROPOSTA = AP.PROPOSTA AND A.NUMERO = AP.NUMERO)
        GROUP BY A.INSTRUTOR 
        ORDER BY SCORE DESC, QTD DESC
        LIMIT 10

-- Para alunos que já tiveram ao menos 1 aula realizada, buscar o username do instrutor com o 
-- qual ele teve mais aulas e a quantidade. Em caso de empate exibir todos os resultados.
-- [Médio - Gabriel]

    -- 1º Retorna a quantidade de aulas que um aluno teve com cada instrutor em ordem crescente
    SELECT  AC.ALUNO, AC.INSTRUTOR, COUNT() 'COUNT'
        FROM ACEITA AC 
        INNER JOIN aula A ON (AC.PROPOSTA = A.PROPOSTA)
        WHERE A.STATUS = 'FINALIZADA'
        GROUP BY AC.ALUNO, AC.INSTRUTOR
        ORDER BY 'COUNT' DESC


    -- 2º Reagrupando em usuário, a primeira coluna é utilizada e ficamos com a maior quantidade.
    SELECT U.NOME_USUARIO 'ALUNO', C.INSTRUTOR, MAX(C.COUNT)
        FROM usuario 'U'
        INNER JOIN (
            SELECT  AC.ALUNO, AC.INSTRUTOR, COUNT(*) 'COUNT'
                FROM ACEITA AC 
                INNER JOIN aula A ON (AC.PROPOSTA = A.PROPOSTA)
                WHERE A.STATUS = 'FINALIZADA'
                GROUP BY AC.ALUNO, AC.INSTRUTOR
                ORDER BY 'COUNT' DESC
        ) 'C' ON (U.NOME_USUARIO = AC.ALUNO)
        GROUP BY U.NOME_USUARIO; 

-- Para cada texto de recomendação de um instrutor, buscar quantas aulas o aluno fez com aquele instrutor

-- Para cada recomendação salva no banco, retornar quantas aulas o aluno responsável pela 
-- recomendação já realizou com o instrutor em questão.
-- [Médio/Difícil]
            
    SELECT R.ALUNO, R.INSTRUTOR, COUNT(*)
        FROM recomenda 'R' 
        INNER JOIN aceita 'AC' ON (AC.ALUNO = R.ALUNO)
        INNER JOIN proposta 'P' ON (AC.PROPOSTA = P.ID AND R.INSTRUTOR = P.INSTRUTOR)
        INNER JOIN aula 'A' ON (A.PROPOSTA = P.ID)
        WHERE A.STATUS = 'FINALIZADA'
        GROUP BY R.ALUNO, R.INSTRUTOR



--------------------------------------------------------
-- INSERTS DE TESTE
--------------------------------------------------------

INSERT INTO usuario VALUES 
('ana', 'ana@instrutora.com', 'senha456', 'Ana', 'Vitória', '', TRUE),
('alice', 'alice@instrutora.com', 'senha457', 'Alice', 'dos Santos', '', TRUE),
('andressa', 'andressa@instrutora.com', 'senha458', 'Andressa', 'Fagundes', '', TRUE),
('amalia', 'amalia@instrutora.com', 'senha459', 'Amália', 'Rodriges', '', TRUE),
('bob', 'bob@aluno.com', 'senha460', 'Bob', 'Milon', '', FALSE),
('carlos', 'carlos@aluno.com', 'senha461', 'Carlos', 'da Silva', '', FALSE),
('diego', 'diego@aluno.com', 'senha462', 'Diego', 'Hernesto', '', FALSE),
('enrique', 'enrique@aluno.com', 'senha463', 'Enrique', 'Cavalcante', '', FALSE),
('felipe', 'felipe@aluno.com', 'senha464', 'Felipe', 'Milos ', '', FALSE),
('gabriel', 'gabriel@aluno.com', 'senha465', 'Gabriel', 'Santos', '', FALSE);

INSERT INTO instrutor VALUES
('ana', 'Formada em 2016, dou aulas particulares para universitários desde 2013.', 'Formada em 2016, dou aulas particulares para universitários desde 2013. Já fui monitora das disciplinas de Cálculo 1 (2016.1, 2016.2), Cálculo 2. Possui experiência.... ', 'Bach. Matemática Aplicada.'),
('alice', 'Formada em 2017, dou aulas particulares para universitários desde 2013.', 'Formada em 2016, dou aulas particulares para universitários desde 2013. Já fui monitora das disciplinas de Cálculo 1 (2016.1, 2016.2), Cálculo 2. Possui experiência.... ', 'Lic. Matemática'),
('andressa', 'Formada em 2018, dou aulas particulares para universitários desde 2013.', 'Formada em 2016, dou aulas particulares para universitários desde 2013. Já fui monitora das disciplinas de Cálculo 1 (2016.1, 2016.2), Cálculo 2. Possui experiência.... ', 'Bach. Ciências da Computação'),
('amalia', 'Estou no ICMC desde 2016 e já fui monitora das disciplinas de ...', 'Formada em 2016, dou aulas particulares para universitários desde 2013. Já fui monitora das disciplinas de Cálculo 1 (2016.1, 2016.2), Cálculo 2. Possui experiência.... ', 'Estudante de Estatística');

INSERT INTO disciplina VALUES
('Línguas',NULL),
('Inglês','Línguas'),
('Francês','Línguas'),
('Alemão','Línguas'),
('Computação',NULL),
('P. O. O.','Computação'),
('Programação Competitiva','Computação'),
('Banco de Dados','Computação'),
('Matemática',NULL),
('Cálculo','Matemática'),
('Estatística','Matemática'),
('Geometria Analítica','Matemática');

INSERT INTO oferecimento VALUES
('ana', 'Inglês', 60.00, 'Teoria Gramatical + Aulas de Conversação'),
('ana', 'Francês', 60.00, 'Teoria Gramatical + Aulas de Conversação'),
('ana', 'Geometria Analítica', 80.00, 'Revisão Teórica, Resolução de Exercícios e Teoremas'),
('ana', 'Cálculo', 80.00, 'Revisão Teórica, Resolução de Exercícios e Teoremas'),
('alice', 'Inglês', 100.00, 'Ajudo à se preparar para o TOEFL e outras provas.'),
('alice', 'Cálculo', 75.00, 'Revisão de questões comuns das provas.'),
('andressa', 'Inglês', 50.00, 'Ajudo à melhorar a conversão por meio de rodas de conversa.'),
('andressa', 'Francês', 50.00, 'Ajudo à melhorar a conversão por meio de rodas de conversa.'),
('andressa', 'Alemão', 50.00, 'Ajudo à melhorar a conversão por meio de rodas de conversa.'),
('amalia', 'Cálculo', 100.00, 'Provas chegando? Ajudo à se preparar para os exames.'),
('amalia', 'Estatística', 80.00, 'Provas chegando? Ajudo à se preparar para os exames.'),
('amalia', 'Geometria Analítica', 80.00, 'Provas chegando? Ajudo à se preparar para os exames.');

INSERT INTO local VALUES
('ana', 'Minha Casa', '3', 'Rua 9 de Julho', '2000', 'Apto. 73', 'Centro', 'São Carlos', 'SP'),
('ana', 'Biblioteca ICMC', '6', 'Av. Trab. São Carlense', '400', 'USP SÂO CARLOS', 'Parque Arnold Schimidt', 'São Carlos', 'SP'),
('ana', 'Biblioteca Física', '12', 'Av. Trab. São Carlense', '400', '', 'Parque Arnold Schimidt', 'São Carlos', 'SP'),
('alice', 'ICMC - Sala Bloco 3', '20', 'Av. Trab. São Carlense', '400', '', 'Parque Arnold Schimidt', 'São Carlos', 'SP'),
('andressa', 'Biblioteca ICMC', '1', 'Av. Trab. São Carlense', '400', 'USP SÂO CARLOS', 'Parque Arnold Schimidt', 'São Carlos', 'SP'),
('andressa', 'Minha Casa', '1', 'Rua 25 de Março', '222', 'Casa 3', 'Cidade Jardim', 'Araraquara', 'SP'),
('amalia', 'Biblioteca ICMC', '6', 'Av. Trab. São Carlense', '400', '', 'Parque Arnold Schimidt', 'São Carlos', 'SP'),
('amalia', 'Minha Casa', '3', 'Rua 27', '27', '', 'Jardim São Paulo', 'Rio Claro', 'SP');
