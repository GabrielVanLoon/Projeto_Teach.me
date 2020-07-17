- selecionar a média de preço base por disciplina
    [Fácil - GroupBy - Tamiris]

SELECT O.DISCIPLINA, ROUND(AVG(O.PRECO_BASE), 2) AS MEDIA
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
    WHERE UPPER(AL.STATUS) = 'AGENDADA' AND PA.ALUNO = 'bob'
	AND AL.DATA_INICIO > CURRENT_TIMESTAMP
	ORDER BY AL.DATA_INICIO;

--otimizado:
SELECT AL.DATA_INICIO, AC.TURMA, AL.INSTRUTOR, AL.PROPOSTA, AL.NUMERO
	FROM AULA AL
    JOIN ACEITA AC ON (AC.PROPOSTA = AL.PROPOSTA) -- para descobrir o usuario
    WHERE UPPER(AL.STATUS) = 'AGENDADA' AND AC.ALUNO = 'bob'
		AND AL.DATA_INICIO > CURRENT_TIMESTAMP
	ORDER BY AL.DATA_INICIO;    
-----------------------------------------------------------------------------------
- Pegar média de nota de um instrutor para cada matéria que ensina (se der aula de mais de uma matéria)
    [Fácil ou Médio? - Junções e group_by - Tamiris]

SELECT PP.DISCIPLINA, ROUND(AVG(AP.NOTA), 2) AS MEDIA_AVALIACAO
    FROM AVALIACAO_PARTICIPANTE AP
    JOIN PROPOSTA PP ON (PP.ID = AP.PROPOSTA)
	WHERE PP.INSTRUTOR = 'ana'
    GROUP BY PP.DISCIPLINA;
-----------------------------------------------------------------------------------
- Listar as turmas que não obtiveram NENHUMA avaliação abaixo de 3 em nenhuma de suas aulas.
    [Média - Tamiris]
--1A FORMA
SELECT DISTINCT PP.TURMA
    FROM PROPOSTA PP
	JOIN AULA AL ON (AL.PROPOSTA = PP.ID)
	WHERE PP.STATUS IN ('APROVADA', 'FINALIZADA')
		AND (AL.STATUS = 'FINALIZADA')
	EXCEPT 
	SELECT PP.TURMA
		FROM PROPOSTA PP
		JOIN AULA AL ON (AL.PROPOSTA = PP.ID)
		WHERE PP.STATUS IN ('APROVADA', 'FINALIZADA')
			AND (AL.NOTA_INSTRUTOR < 3)

-- 2A FORMA - MAIS EFICIENTE
SELECT PP.TURMA
    FROM PROPOSTA PP
	JOIN AULA AL ON (AL.PROPOSTA = PP.ID)
	WHERE PP.STATUS IN ('APROVADA', 'FINALIZADA')
		AND AL.NOTA_INSTRUTOR IS NOT NULL
	GROUP BY PP.TURMA
	HAVING MIN (AL.NOTA_INSTRUTOR) > 3
-----------------------------------------------------------------------------------
- Instrutores que deram a maior quantidade de aulas em cada estado no último mês.
    [Médio - Dificil- Tamiris]
--select interno, exibe a quantidade de aulas por instrutor em cada estado
SELECT AL.INSTRUTOR, L.UF, COUNT (AL.NUMERO)
	FROM LOCAL L
	JOIN AULA AL ON (L.INSTRUTOR = AL.INSTRUTOR AND L.NOME = AL.LOCAL)
	WHERE (AL.STATUS = 'FINALIZADA')
		AND AL.DATA_INICIO >= ('now'::timestamp - '1 month'::interval)
	GROUP BY AL.INSTRUTOR, L.UF
	ORDER BY L.UF, COUNT (AL.NUMERO) DESC

--query completa, seleciona apenas as maiores quantidades de aulas
SELECT TODOS.UF, (array_agg(TODOS.INSTRUTOR))[1], MAX (TODOS.N_AULAS)	
	FROM (
		SELECT AL.INSTRUTOR, L.UF, COUNT (AL.NUMERO) AS N_AULAS
			FROM LOCAL L
			JOIN AULA AL ON (L.INSTRUTOR = AL.INSTRUTOR AND L.NOME = AL.LOCAL)
			WHERE (AL.STATUS = 'FINALIZADA')
				AND AL.DATA_INICIO >= ('now'::timestamp - '1 month'::interval)
			GROUP BY AL.INSTRUTOR, L.UF
			ORDER BY L.UF, COUNT (AL.NUMERO) DESC )
	AS TODOS
	GROUP BY TODOS.UF