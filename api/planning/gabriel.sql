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

INSERT INTO horario_disponivel VALUES
('ana', 'SEG', '14:00'),
('ana', 'SEG', '15:00'),
('ana', 'SEG', '16:00'),
('ana', 'SEG', '17:00'),
('ana', 'SEG', '18:00'),
('ana', 'SEG', '19:00'),
('ana', 'QUA', '16:00'),
('ana', 'QUA', '17:00'),
('ana', 'QUA', '18:00'),
('ana', 'QUA', '19:00');

INSERT INTO turma VALUES
('ana', '', '', '', 1, 1, 'PARTICULAR'),
('alice', '', '', '', 1, 1, 'PARTICULAR'),
('andressa', '', '', '', 1, 1, 'PARTICULAR'),
('amalia', '', '', '', 1, 1, 'PARTICULAR'),
('bob', '', '', '', 1, 1, 'PARTICULAR'),
('carlos', '', '', '', 1, 1, 'PARTICULAR'),
('diego', '', '', '', 1, 1, 'PARTICULAR'),
('enrique', '', '', '', 1, 1, 'PARTICULAR'),
('felipe', '', '', '', 1, 1, 'PARTICULAR'),
('gabriel', '', '', '', 1, 1, 'PARTICULAR'),
('grupo_linguas', 'Os Poliglotas', 'Grupo para insteressandos no aprendizado e estudo de multiplas línguas', 'img.jpg', 6, 10, 'EM AULAS'),
('grupo_exatas018', 'SMA (Socorro Meu Amigo)!!', 'Grupo da 018 para estudar pras provas do SMA', 'img.jpg', 3, 5, 'BUSCANDO INSTRUTOR'),
('grupo_compsofre', 'Viva Alan Turing!!', 'Grupo pra discutir sobre a vida e afins', 'img.jpg', 4, 4, 'BUSCANDO INSTRUTOR'),
('grupo_random', 'Just a Random Team', 'Description? ', 'img.jpg', 2, 20, 'ENCERRADA');

INSERT INTO participante VALUES
('bob', 'grupo_linguas', TRUE),
('carlos', 'grupo_linguas', FALSE),
('diego', 'grupo_linguas', FALSE),
('enrique', 'grupo_linguas', FALSE),
('felipe', 'grupo_linguas', FALSE),
('gabriel', 'grupo_linguas', FALSE),
('diego', 'grupo_exatas018', TRUE),
('enrique', 'grupo_exatas018', FALSE),
('felipe', 'grupo_exatas018', FALSE),
('diego', 'grupo_compsofre', TRUE),
('felipe', 'grupo_compsofre', FALSE),
('gabriel', 'grupo_compsofre', FALSE),
('bob', 'grupo_compsofre', FALSE);

INSERT INTO proposta VALUES
(10, 'grupo_linguas', 'ana', 'Inglês', 1, 'RECUSADA', '2020-03-15 12:30:00', 100),
(11, 'grupo_linguas', 'ana', 'Inglês', 2, 'FINALIZADA', '2020-04-15 12:30:00', 80),
(12, 'grupo_linguas', 'ana', 'Inglês', 3, 'APROVADA', '2020-06-15 12:30:00', 80),
(13, 'grupo_linguas', 'ana', 'Francês', 4, 'RECUSADA', '2020-06-15 12:30:00', 90),
(14, 'grupo_linguas', 'ana', 'Francês', 5, 'APROVADA', '2020-06-23 12:30:00', 180),
(15, 'grupo_linguas', 'alice', 'Inglês', 1, 'APROVADA', '2020-07-03 12:30:00', 100),
(16, 'grupo_linguas', 'andressa', 'Alemão', 1, 'APROVADA', '2020-07-03 12:30:00', 80),
(17, 'grupo_exatas018', 'ana', 'Geometria Analítica', 1, 'FINALIZADA', '2020-07-06 12:30:00', 120),
(18, 'grupo_exatas018', 'ana', 'Cálculo', 2, 'APROVADA', '2020-07-06 14:30:00', 80),
(19, 'grupo_exatas018', 'amalia', 'Estatística', 1, 'APROVADA', '2020-07-06 14:30:00', 60),
(20, 'grupo_exatas018', 'amalia', 'Geometria Analítica', 2, 'APROVADA', '2020-07-07 14:30:00', 90),
(21, 'grupo_compsofre', 'amalia', 'Estatística', 1, 'APROVADA', '2020-07-16 14:30:00', 60),
(22, 'grupo_compsofre', 'amalia', 'Geometria Analítica', 2, 'APROVADA', '2020-07-16 14:30:00', 90);


INSERT INTO aula VALUES 
(10, 1, 'ana', 'Biblioteca ICMC', 100, 'CANCELADA', '2020-03-17 14:30:00', '2020-03-17 16:30:00', NULL),
(11, 1, 'ana', 'Biblioteca ICMC', 80, 'FINALIZADA', '2020-04-17 14:30:00', '2020-04-17 16:30:00', 5),
(12, 1, 'ana', 'Biblioteca ICMC', 80, 'AGENDADA', '2020-06-21 13:00:00', '2020-06-21 17:30:00', NULL),
(13, 1, 'ana', 'Biblioteca ICMC', 90, 'CANCELADA', '2020-06-22 13:00:00', '2020-06-22 15:30:00', NULL),
(14, 1, 'ana', 'Biblioteca ICMC', 60, 'FINALIZADA', '2020-06-24 13:00:00', '2020-06-24 16:30:00', 5),
(14, 2, 'ana', 'Biblioteca ICMC', 60, 'FINALIZADA', '2020-06-25 13:00:00', '2020-06-25 16:00:00', 5),
(14, 3, 'ana', 'Biblioteca ICMC', 60, 'AGENDADA', '2020-07-25 14:00:00', '2020-07-25 18:00:00', NULL),
(15, 1, 'alice', 'ICMC - Sala Bloco 3', 100, 'FINALIZADA', '2020-07-04 13:00:00', '2020-07-04 19:00:00', 5),
(16, 1, 'andressa', 'Biblioteca ICMC', 80, 'FINALIZADA', '2020-07-05 13:00:00', '2020-07-05 19:00:00', 4),
(17, 1, 'ana', 'Biblioteca ICMC', 60, 'FINALIZADA', '2020-07-10 13:00:00', '2020-07-10 17:00:00', NULL),
(17, 2, 'ana', 'Biblioteca ICMC', 60, 'FINALIZADA', '2020-07-11 13:00:00', '2020-07-11 17:00:00', NULL),
(18, 1, 'ana', 'Biblioteca ICMC', 80, 'AGENDADA', '23/07/2020 13:00:00', '23/07/2020 17:00:00', NULL),
(21, 1, 'amalia', 'Minha Casa', 60, 'CANCELADA', '2020-07-16 14:30:00', '2020-07-16 15:30:00', NULL),
(22, 1, 'amalia', 'Minha Casa', 90, 'AGENDADA', '2020-07-22 14:30:00', '2020-07-22 17:30:00', NULL);

INSERT INTO aceita VALUES  
('bob', 'grupo_linguas', 11),
('carlos', 'grupo_linguas', 11),
('diego', 'grupo_linguas', 11),
('enrique', 'grupo_linguas', 11),
('felipe', 'grupo_linguas', 11),
('gabriel', 'grupo_linguas', 11),
('bob', 'grupo_linguas', 12),
('carlos', 'grupo_linguas', 12),
('diego', 'grupo_linguas', 12),
('enrique', 'grupo_linguas', 12),
('felipe', 'grupo_linguas', 12),
('gabriel', 'grupo_linguas', 12),
('bob', 'grupo_linguas', 14),
('carlos', 'grupo_linguas', 14),
('diego', 'grupo_linguas', 14),
('enrique', 'grupo_linguas', 14),
('felipe', 'grupo_linguas', 14),
('gabriel', 'grupo_linguas', 14),
('bob', 'grupo_linguas', 15),
('carlos', 'grupo_linguas', 15),
('diego', 'grupo_linguas', 15),
('enrique', 'grupo_linguas', 15),
('felipe', 'grupo_linguas', 15),
('gabriel', 'grupo_linguas', 15),
('bob', 'grupo_linguas', 16),
('carlos', 'grupo_linguas', 16),
('diego', 'grupo_linguas', 16),
('enrique', 'grupo_linguas', 16),
('felipe', 'grupo_linguas', 16),
('gabriel', 'grupo_linguas', 16),
('diego', 'grupo_exatas018', 17),
('enrique', 'grupo_exatas018', 17),
('felipe', 'grupo_exatas018', 17),
('diego', 'grupo_exatas018', 18),
('enrique', 'grupo_exatas018', 18),
('felipe', 'grupo_exatas018', 18),
('diego', 'grupo_exatas018', 19),
('enrique', 'grupo_exatas018', 19),
('felipe', 'grupo_exatas018', 19),
('diego', 'grupo_exatas018', 20),
('enrique', 'grupo_exatas018', 20),
('felipe', 'grupo_exatas018', 20),
('diego', 'grupo_compsofre', 21),
('felipe', 'grupo_compsofre', 21),
('gabriel', 'grupo_compsofre', 21),
('bob', 'grupo_compsofre', 21),
('diego', 'grupo_compsofre', 22),
('felipe', 'grupo_compsofre', 22),
('gabriel', 'grupo_compsofre', 22),
('bob', 'grupo_compsofre', 22);

INSERT INTO avaliacao_participante VALUES 
('bob', 'grupo_linguas', 11, 1, 5),
('carlos', 'grupo_linguas', 11, 1, 5),
('diego', 'grupo_linguas', 11, 1, 4),
('bob', 'grupo_linguas', 14, 1, 5),
('carlos', 'grupo_linguas', 14, 1, 3),
('diego', 'grupo_linguas', 14, 1, 4),
('enrique', 'grupo_linguas', 14, 2, 5),
('felipe', 'grupo_linguas', 14, 2, 5),
('diego', 'grupo_exatas018', 17, 1, 5),
('enrique', 'grupo_exatas018', 17, 1, 5),
('felipe', 'grupo_exatas018', 17, 1, 5),
('carlos', 'grupo_linguas', 16, 1, 5),
('diego', 'grupo_linguas', 16, 1, 5),
('felipe', 'grupo_linguas', 16, 1, 5),
('gabriel', 'grupo_linguas', 16, 1, 5);

INSERT INTO chat VALUES 
('grupo_linguas', 1, 'Chat Interno @grupo_linguas', 'ATIVO', NULL),
('grupo_exatas018', 1, 'Chat Interno @grupo_exatas018', 'ATIVO', NULL),
('grupo_compsofre', 1, 'Chat Interno @grupo_compsofre', 'ATIVO', NULL),
('grupo_random', 1, 'Chat Interno @grupo_random', 'ATIVO', NULL),
('grupo_linguas', 2, 'Negociação @grupo_linguas', 'ATIVO', 'ana'),
('grupo_linguas', 3, 'Negociação @grupo_linguas', 'ATIVO', 'alice'),
('grupo_linguas', 4, 'Negociação @grupo_linguas', 'ATIVO', 'andressa'),
('grupo_exatas018', 2, 'Negociação @grupo_compsofre', 'ATIVO', 'ana'),
('grupo_exatas018', 3, 'Negociação @grupo_compsofre', 'ARQUIVADO', 'alice'),
('grupo_exatas018', 4, 'Negociação @grupo_compsofre', 'ATIVO', 'amalia'),
('grupo_compsofre', 2, 'Negociação @grupo_compsofre', 'ATIVO', 'amalia'),
('grupo_compsofre', 3, 'Negociação @grupo_compsofre', 'ARQUIVADO', 'ana'),
('grupo_random', 2, 'Negociação @grupo_random', 'ATIVO', 'amalia'),
('bob', 1, 'Negociação @bot', 'ATIVO', 'ana');

INSERT INTO recomenda VALUES
('bob', 'ana', 'A Ana é uma instrutora incrível. Foi super atenciosa comigo e minha turma mesmo em momentos de maior dificuldade. Recomendo!!!'),
('carlos', 'ana', 'Já tive diversas aulas com a Ana e ela sempre foi uma pessoa muito calma e com uma didática incrível!'),
('diego', 'ana', 'Pessoal, pode confiar na review do pai aqui. Professora T0P e Dedicada!!!'),
('felipe', 'amalia', 'Me ajudou bastante nas matérias de GA e estatística!');