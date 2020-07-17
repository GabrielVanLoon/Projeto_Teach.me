- selecionar a média de preço base por disciplina
    [Fácil - GroupBy - Tamiris]

SELECT AVG(O.PRECO_BASE), O.DISCIPLINA
    FROM OFERECIMENTO O
    GROUP BY O.DISCIPLINA;
-----------------------------------------------------------------------------------
- Buscar dados do usuario e, se ele for instrutor, buscar também seus dados de instrutor
    [Fácil - Junção externa - Tamiris]

SELECT U.NOME_USUARIO, U.EMAIL, U.NOME, U.SOBRENOME, I.RESUMO, I.SOBRE_MIM, I.FORMACAO
    FROM USUARIO U 
    LEFT JOIN INSTRUTOR I 
    ON (U.NOME_USUARIO = I.NOME_USUARIO);
-----------------------------------------------------------------------------------
- Mostrar as aulas do usuario que ainda irão ocorrer, ordenadas a partir da data mais próxima
    [Fácil - Tamiris]

SELECT AL.DATA_INICIO, PP.TURMA, PP.DISCIPLINA, AL.INSTRUTOR --, PA.ALUNO
	FROM AULA AL
    JOIN PROPOSTA PP ON (AL.PROPOSTA = PP.ID) -- para descobrir a turma
    JOIN PARTICIPANTE PA ON (PA.TURMA = PP.TURMA) -- para descobrir o usuario
    WHERE UPPER(AL.STATUS) = 'AGENDADA' AND UPPER(PA.ALUNO) = 'BOB'
	AND AL.DATA_INICIO > CURRENT_TIMESTAMP
	ORDER BY AL.DATA_INICIO;
-----------------------------------------------------------------------------------
- Pegar média de nota de instrutor para cada matéria que ensina (se der aula de mais de uma matéria)
    [Fácil ou Médio? - Junções e group_by - Tamiris]

SELECT AVG(AP.NOTA), PP.DISCIPLINA
    FROM AVALIACAO_PARTICIPANTE AP
    JOIN PROPOSTA PP ON (PP.ID = AP.PROPOSTA)
	WHERE UPPER(PP.INSTRUTOR) = 'ANA'
    GROUP BY PP.DISCIPLINA;
-----------------------------------------------------------------------------------
- Listar as turmas que não obtiveram NENHUMA avaliação abaixo de 3 em nenhuma de suas aulas.
    [Média - Tamiris]

SELECT T.NOME_TURMA
    FROM TURMA T
    JOIN PROPOSTA P ON (T.NOME = P.TURMA)
    JOIN AULA A ON (P.ID = A.PROPOSTA)
    WHERE MIN (A.NOTA_INSTRUTOR > 3.0);
-----------------------------------------------------------------------------------
- Instrutores que deram a maior quantidade de aulas em cada estado no último mês. Em casos de empate exibir todos.
    [Médio - Tamiris]

SELECT I.NOME_USUARIO, COUNT (AL.NUMERO)
    FROM INSTRUTOR I
    JOIN AULA AL ON (AL.INSTRUTOR = I.NOME_USUARIO)
    WHERE (AL.STATUS = 'FINALIZADA');