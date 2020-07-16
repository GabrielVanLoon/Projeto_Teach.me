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