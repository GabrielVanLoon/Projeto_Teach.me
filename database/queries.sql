-- Script:      queries.sql
-- Descrição:   Consultas de complexidade média ou superior que foram levantadas e
--              implementadas. Algumas consultas possuem uma ou mais variaçõe que foram
--              levantadas e depois analizadas a fim de verificar o planejamento mais 
--              eficiente utlizada pelo postgre.
--              Obs: As queries foram ordenadas com complexidade crescente.
-- Data:        14/07/2020 
-- Versão:      1.0.0


-- 1) Selecionar a média do preço base das disciplinas que já são oferecidas 
-- por ao menos um instrutor dentro da plataforma.

SELECT O.DISCIPLINA, ROUND(AVG(O.PRECO_BASE), 2) AS MEDIA
    FROM OFERECIMENTO O
    GROUP BY O.DISCIPLINA;


-- 2) Buscar dados do usuario e, se ele for instrutor, buscar também seus dados de instrutor

SELECT U.NOME_USUARIO, U.EMAIL, U.NOME, U.SOBRENOME, I.RESUMO, I.SOBRE_MIM, I.FORMACAO
    FROM USUARIO U 
    LEFT JOIN INSTRUTOR I 
    ON (U.NOME_USUARIO = I.NOME_USUARIO);


-- 3) Selecionar, para todas as turmas existentes, a quantidade de aulas já realizadas até 
-- o momento. Se uma turma ainda não realizou nenhuma aula o resultado deve ser zero.

  SELECT T.NOME, COUNT(A.NUMERO)
    FROM  proposta P
    INNER JOIN aula A ON  (P.ID = A.PROPOSTA AND A.STATUS = 'FINALIZADA')
    RIGHT JOIN turma T ON (P.TURMA = T.NOME)
    GROUP BY T.NOME;


-- 4) Selecionar nome_usuario, nome, nome da disciplina, preço base e metodologia dos instrutores que
-- realizam aulas em uma cidade, possuem disponibilidade no horário indicado e cujo preço base
-- da disciplina solicitada esteja dentro de um intervalo de preço pré-definido.
-- (Busca de instrutores utilizando o máximo de filtros disponível)

    SELECT DISTINCT U.NOME_USUARIO, U.NOME, O.DISCIPLINA, O.PRECO_BASE, O.METODOLOGIA
        FROM oferecimento O
        INNER JOIN usuario U ON (O.INSTRUTOR = U.NOME_USUARIO)
        INNER JOIN local L ON (O.INSTRUTOR = L.INSTRUTOR)
        INNER JOIN horario_disponivel HR ON (O.INSTRUTOR = HR.INSTRUTOR)
        WHERE  O.DISCIPLINA = 'Cálculo' AND O.PRECO_BASE > 0.00 AND O.PRECO_BASE < 100.00
            AND L.CIDADE = 'São Carlos' AND L.UF = 'SP' 
            AND HR.DIA_SEMANA = 'SEG' AND HR.HORARIO = '14:00'
    
    -- Sobre:: Precisa do distinct pq caso o usuário cadastre multiplos locais com o mesmo 
    -- par (cidade, uf) o mesmo instrutor é retornado diversas vezes.
    -- 
    -- Possível melhoria no modelo: Separar o relacionamento Local em Local,Espaço
    -- Local  -> Cidade, UF.
    -- Espaço -> Cidade, UF, Nome, rua, número, complemento, bairro.


-- 5) Selecionar, para cada turma existente na base de dados, a quantidade total de propostas
-- FINALIZADAS ou APROVADAS cujo preço total das aulas foi superior ou igual à R$ 100.00.

    SELECT T.NOME, COUNT(P.ID) QUANTIDADE
        FROM turma T
		LEFT JOIN ( SELECT P.ID, P.TURMA
				FROM PROPOSTA P
				WHERE P.PRECO_TOTAL >= 100.00 AND P.STATUS IN ('FINALIZADA','APROVADA')
			) P ON (T.NOME = P.TURMA)
		GROUP BY T.NOME;
    -- Sobre: Utilizando Sub-Queries para filtrar as propostas e remover a necessidade
    -- de utilizar o WHERE (P.ID IS NULL).


-- 6) Retornar a quantidade de horas que cada instrutor do sistema deu de aula nos últimos 30 dias.

    SELECT P.INSTRUTOR, SUM(A.DATA_FIM - A.DATA_INICIO) 
        FROM aula A
        INNER JOIN proposta P ON (A.PROPOSTA = P.ID)
        WHERE A.STATUS = 'FINALIZADA' 
            AND A.DATA_INICIO >= ('now'::timestamp - '1 month'::interval)
        GROUP BY P.INSTRUTOR;
    -- Sobre: O Postgresql possui o sistema de subtração entre datas e intervalos 
    -- que tornaram a query mais limpa e simples do que eu esperava.


-- 7) Retornar o username e o score dos 10 instrutores com a maior média de avaliação na plataforma. 
-- Em caso de empate o desempate  deve ser feito pela quantidade de aulas dadas.
    
    SELECT A.INSTRUTOR, ROUND(AVG(AP.NOTA), 2) SCORE, COUNT(DISTINCT ROW(A.PROPOSTA, A.NUMERO)) QTD
        FROM aula A
        INNER JOIN avaliacao_participante AP ON (A.PROPOSTA = AP.PROPOSTA AND A.NUMERO = AP.NUMERO)
        GROUP BY A.INSTRUTOR 
        ORDER BY SCORE DESC, QTD DESC
        LIMIT 10
    -- Sobre: O fato da chave primária de aula ser composta aumentou um pouco o custo do
    -- desempate devido ao fato de ser necessário realizar um DISTINCT.


-- 8) Para alunos que já tiveram ao menos 1 aula realizada, buscar o username do instrutor com  
-- o qual ele teve mais aulas e a quantidade. Em caso de empate retornar qualquer um dos resultados.

    SELECT T.ALUNO, (array_agg(T.INSTRUTOR ORDER BY T.COUNT DESC))[1], MAX(T.COUNT) 
        FROM 
            ( SELECT  AC.ALUNO, A.INSTRUTOR, COUNT(*) COUNT
                FROM ACEITA AC 
                INNER JOIN aula A ON (AC.PROPOSTA = A.PROPOSTA)
                WHERE A.STATUS = 'FINALIZADA'
                GROUP BY AC.ALUNO, A.INSTRUTOR
                ORDER BY COUNT DESC ) AS T
        GROUP BY T.ALUNO;


-- 9) Para cada recomendação salva no banco, retornar quantas aulas o aluno responsável pela 
-- recomendação já realizou com o instrutor em questão.
            
	SELECT R.ALUNO, R.INSTRUTOR, COUNT(*)
        FROM recomenda R 
        INNER JOIN aceita AC ON (R.ALUNO = AC.ALUNO)
        INNER JOIN proposta P ON (AC.PROPOSTA = P.ID AND R.INSTRUTOR = P.INSTRUTOR)
        INNER JOIN aula A ON (A.PROPOSTA = P.ID)
        WHERE A.STATUS = 'FINALIZADA'
        GROUP BY R.ALUNO, R.INSTRUTOR;
    -- Sobre: joins um pouco fora do convencional que se aproveitam do fato das chaves serem
    -- semânticas para serem otimizados e garantirem que apenas as propostas ligados ao mesmo aluno
    -- e professor de recomenda são contadas.


-- 10) Buscar as futuras aulas já agendadas de um aluno ordenando da aula mais próxima à mais
-- distante. Retornar a data da aula, o nome da turma, a disciplina da aula e o instrutor responsável.

	SELECT AL.DATA_INICIO, AC.TURMA, AL.INSTRUTOR, AL.PROPOSTA, AL.NUMERO
		FROM AULA AL
		JOIN ACEITA AC ON (AC.PROPOSTA = AL.PROPOSTA) -- para descobrir o usuario
		WHERE UPPER(AL.STATUS) = 'AGENDADA' AND AC.ALUNO = 'bob'
			AND AL.DATA_INICIO > CURRENT_TIMESTAMP
		ORDER BY AL.DATA_INICIO;    


-- 11) Dado um instrutor, retornar a média das avaliações que ele recebeu para cada matéria que
-- ele oferece e que já recebeu ao menos 1 avaliação.

    SELECT PP.DISCIPLINA, ROUND(AVG(AP.NOTA), 2) AS MEDIA_AVALIACAO
        FROM AVALIACAO_PARTICIPANTE AP
        JOIN PROPOSTA PP ON (PP.ID = AP.PROPOSTA)
        WHERE PP.INSTRUTOR = 'ana'
        GROUP BY PP.DISCIPLINA;


-- 12) Listar todas as turmas do sistema que não obtiveram NENHUMA avaliação abaixo de 3 de seus
-- instrutores nas aulas realizadas. Aulas não avaliadas pelo instrutor devem ser ignoradas.

	SELECT PP.TURMA
		FROM PROPOSTA PP
		JOIN AULA AL ON (AL.PROPOSTA = PP.ID)
		WHERE PP.STATUS IN ('APROVADA', 'FINALIZADA')
			AND AL.NOTA_INSTRUTOR IS NOT NULL
		GROUP BY PP.TURMA
		HAVING MIN (AL.NOTA_INSTRUTOR) > 3


-- 13) Exibir o instrutor que realizou a maior quantidade de aulas no último mês em cada
-- estado. Em caso de empate exibir qualquer um dos possíveis resultados.

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


-- 14) Dado um aluno no banco, selecionar as aulas que ele já participou mas ainda não avaliou.

  SELECT PR.TURMA, PR.INSTRUTOR, PR.DISCIPLINA, AU.NUMERO AS NUMERO_AULA
    FROM aceita AC
    INNER JOIN proposta PR ON (AC.PROPOSTA = PR.ID AND PR.STATUS IN ('APROVADA', 'FINALIZADA'))
    INNER JOIN aula AU ON (AU.PROPOSTA = AC.PROPOSTA AND AU.STATUS = 'FINALIZADA')
    LEFT JOIN avaliacao_participante AP ON (AP.ALUNO = AC.ALUNO AND AP.TURMA = AC.TURMA AND AP.PROPOSTA = AU.PROPOSTA AND AP.NUMERO = AU.NUMERO)
	WHERE AC.ALUNO = 'felipe' AND AP.NOTA IS NULL; 


-- 15) Dado um aluno no banco, selecionar os instrutores cujas aulas foram 
-- avaliadas com nota 4 ou superior pelo aluno, mas não foram recomendados pelo mesmo.

SELECT DISTINCT AU.INSTRUTOR
  FROM aceita AC
  INNER JOIN aula AU ON (AU.PROPOSTA = AC.PROPOSTA)
  INNER JOIN avaliacao_participante AP ON (AP.ALUNO = AC.ALUNO AND AP.TURMA = AC.TURMA AND AP.PROPOSTA = AU.PROPOSTA AND AP.NUMERO = AU.NUMERO)
  LEFT JOIN recomenda RE ON (RE.ALUNO = AC.ALUNO AND RE.INSTRUTOR = AU.INSTRUTOR)
  WHERE AC.ALUNO = 'enrique' AND RE.ALUNO IS NULL AND AP.NOTA >= 4;


-- 16) Exibir a média global de mensagens trocadas entre instrutores e lideres de turma
-- em chats de negociação até a realização da primeira iteração de proposta na aplicação

    SELECT AVG(CONTAGEM.COUNT) AS MSG_ANTES_PROPOSTA
    FROM (SELECT P.TURMA, P.INSTRUTOR, COUNT(*)
        FROM chat C
        INNER JOIN (SELECT P.TURMA, P.INSTRUTOR, MIN(P.DATA_CRIACAO)
                        FROM proposta P
                        GROUP BY P.TURMA, P.INSTRUTOR
                    ) P ON (P.TURMA = C.TURMA AND P.INSTRUTOR = C.INSTRUTOR)
        INNER JOIN mensagem M ON (C.TURMA = M.TURMA AND C.CODIGO = M.CODIGO)
        WHERE C.INSTRUTOR IS NOT NULL AND M.DATA_ENVIO <= P.MIN
        GROUP BY P.TURMA, P.INSTRUTOR
    ) CONTAGEM;


-- 17) Selecionar todos os instrutores que já deram aulas de TODAS as disciplinas 
-- filhas de uma disciplina pré-especificada (neste caso 'Computação')
-- (Exemplo de Divisão )
SELECT DISTINCT O.INSTRUTOR
    FROM oferecimento O
    WHERE O.INSTRUTOR not in ( 
        SELECT resto.INSTRUTOR FROM (
            -- Todas combinações possíveis dos Instrutores com TODAS disciplinas filhas de 'Computação'
            (SELECT sp.INSTRUTOR , p.DISCIPLINA 
                    FROM (select D.NOME DISCIPLINA from disciplina D WHERE D.DISCIPLINA_PAI = 'Computação') as p 
                    CROSS JOIN (select distinct O.INSTRUTOR from oferecimento O) as sp
            )
            EXCEPT -- Operação MINUS de conjuntos
            -- Combinações existentes de instrutores e disciplina 
            (SELECT O.INSTRUTOR , O.DISCIPLINA FROM oferecimento O, disciplina D WHERE (O.DISCIPLINA = D.NOME AND D.DISCIPLINA_PAI = 'Computação')) 
        )  AS resto 
    ); 