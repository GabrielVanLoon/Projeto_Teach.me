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
        GROUP BY P.TURMA 
        WHERE P.PRECO_TOTAL >= 100.00 AND (P.STATUS = 'FINALIZADA' OR P.STATUS = 'APROVADA')