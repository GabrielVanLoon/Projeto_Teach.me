- selecionar a média de preço base por disciplina
    [Fácil - GroupBy - Tamiris]

SELECT AVG(OF.PRECO_BASE)
    FROM OFERECIMENTO 'OF'
    GROUP BY OF.DISCIPLINA;

-----------------------------------------------------------------------------------


- Buscar dados do usuario e, se ele for instrutor, buscar também seus dados de instrutor
    [Fácil - Junção externa - Tamiris]

SELECT U.NOME_USUARIO, U.EMAIL, U.NOME, U.SOBRENOME, I.RESUMO, I.SOBRE_MIM, I.FORMACAO
    FROM USUARIO 'U' 
    LEFT JOIN INSTRUTOR 'I' 
    ON (U.NOME_USUARIO = I.NOME_USUARIO);


-----------------------------------------------------------------------------------

- Mostrar as aulas do usuario que ainda irão ocorrer, ordenadas a partir da data mais próxima
    [Fácil - Tamiris]

-- ATRIBUTOS DE AULA
-- A.PROPOSTA, A.NUMERO, A.INSTRUTOR, A.LOCAL, A.PRECO_FINAL, A.STATUS, A.DATA_INICIO, A.DATA_FIM, A.NOTA_INSTRUTOR
SELECT A.PROPOSTA, A.NUMERO, A.INSTRUTOR, A.LOCAL, A.DATA_INICIO, A.DATA_FIM
    FROM AULA 'A'
    WHERE UPPER(A.STATUS) = 'AGENDADA'
    JOIN PROPOSTA 'P' ON (A.PROPOSTA = P.ID)
    JOIN ACEITA 'AC' ON (AC.PROPOSTA = P.ID)
    ORDER BY A.DATA_INICIO;

-----------------------------------------------------------------------------------

- Pegar média de nota de instrutor para cada matéria que ensina (se der aula de mais de uma matéria)
    [Fácil ou Médio? - Junções e group_by - Tamiris]

SELECT AVG(AP.NOTA)
    FROM AVALIACAO_PARTICIPANTE 'AP'
    JOIN PROPOSTA 'P' ON (P.ID = AP.PROPOSTA)
    GROUP BY P.DISCIPLINA;

-----------------------------------------------------------------------------------

- Listar as turmas que não obtiveram NENHUMA avaliação abaixo de 3 em nenhuma de suas aulas.
    [Média - Tamiris]


SELECT T.NOME_TURMA
    FROM TURMA 'T'
    WHERE T.SITUACAO = ATIVA

MIN (Nota) > 3.0

-----------------------------------------------------------------------------------

- Instrutores que deram a maior quantidade de aulas em cada estado no último mês. Em casos de empate exibir todos.
    [Médio - Tamiris]

SELECT 