-- Selecionar a média do preso base das disciplinas que já são oferecidas por ao
-- menos um instrutor dentro da plataforma.

SELECT O.DISCIPLINA, ROUND(AVG(O.PRECO_BASE), 2) AS MEDIA
    FROM OFERECIMENTO O
    GROUP BY O.DISCIPLINA;

-----------------------------------------------------------------------------------

-- [PASS] Buscar dados do usuario e, se ele for instrutor, buscar também seus dados de instrutor
-- Fácil [Fácil - Junção externa - Tamiris]

SELECT U.NOME_USUARIO, U.EMAIL, U.NOME, U.SOBRENOME, I.RESUMO, I.SOBRE_MIM, I.FORMACAO
    FROM USUARIO U 
    LEFT JOIN INSTRUTOR I 
    ON (U.NOME_USUARIO = I.NOME_USUARIO);

-----------------------------------------------------------------------------------

-- Buscar as futuras aulas já agendadas de um aluno ordenadondo da aula mais próxima à mais
-- distante. Retornar a data da aula, o nome da turma, a disciplina da aula e o instrutor responsável.

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

-- Dado um instrutor, retorna a média das avaliações que ele recebe para cada matéria que
-- ele oferece e que já recebeu ao menos 1 avaliação.

SELECT PP.DISCIPLINA, ROUND(AVG(AP.NOTA), 2) AS MEDIA_AVALIACAO
    FROM AVALIACAO_PARTICIPANTE AP
    JOIN PROPOSTA PP ON (PP.ID = AP.PROPOSTA)
	WHERE PP.INSTRUTOR = 'ana'
    GROUP BY PP.DISCIPLINA;

-----------------------------------------------------------------------------------

-- Listar todas as turmas do sistema que não obtiveram NENHUMA avaliação abaixo de 3 de seus
-- instrutores nas aulas realizadas. Aulas não avaliadas pelo instrutor devem ser ignoradas.

	-- 1ª Forma - Utilizando subtração de conjuntos
	-- Foi a primeira forma pensada, porém extremamente ineficiente e deixamos de lado.
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

	-- 2ª Forma - Utilizando GROUP BY + HAVING
	-- Muito mais eficiente, segundo a análise do sgbd.
	SELECT PP.TURMA
		FROM PROPOSTA PP
		JOIN AULA AL ON (AL.PROPOSTA = PP.ID)
		WHERE PP.STATUS IN ('APROVADA', 'FINALIZADA')
			AND AL.NOTA_INSTRUTOR IS NOT NULL
		GROUP BY PP.TURMA
		HAVING MIN (AL.NOTA_INSTRUTOR) > 3

-----------------------------------------------------------------------------------

-- Exibir o instrutor que realizou a maior quantidade de aulas no último mês em cada
-- estado. Em caso de empate exibir qualquer um dos possíveis resultados.

	-- Consulta Interna: Retorna a quantidade de aulas que cada 
	-- instrutor deu em cada estado e a ordena em ordem decrescente pela contagem. 
	SELECT AL.INSTRUTOR, L.UF, COUNT (AL.NUMERO)
		FROM LOCAL L
		JOIN AULA AL ON (L.INSTRUTOR = AL.INSTRUTOR AND L.NOME = AL.LOCAL)
		WHERE (AL.STATUS = 'FINALIZADA')
			AND AL.DATA_INICIO >= ('now'::timestamp - '1 month'::interval)
		GROUP BY AL.INSTRUTOR, L.UF
		ORDER BY L.UF, COUNT (AL.NUMERO) DESC

	-- Consulta Externa: Reagrupa os resultados por estado e exibe a quantidade
	-- máxima de cada grupo junto do primeiro instrutor de cada agrupamento.
	-- Como a consulta interna é ordenada, é garantido que o primeiro instrutor
	-- sempre será o que realizou a maior quantidade de aulas. 
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