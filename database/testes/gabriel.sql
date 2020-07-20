-- 1) Selecionar nome_usuario, nome, nome da disciplina, preço base e metodologia dos instrutores que
-- realizam aulas em uma cidade, possuem disponibilidade no horário indicado e cujo valor base
-- da disciplina solicitada esteja dentro de um intervalo de preço pré-definido.
--

    SELECT DISTINCT U.NOME_USUARIO, U.NOME, O.DISCIPLINA, O.PRECO_BASE, O.METODOLOGIA -- , L.NOME,  L.CIDADE, L.UF, HR.dia_semana, HR.horario
        FROM oferecimento O
        INNER JOIN usuario U ON (O.INSTRUTOR = U.NOME_USUARIO)
        INNER JOIN local L ON (O.INSTRUTOR = L.INSTRUTOR)
        INNER JOIN horario_disponivel HR ON (O.INSTRUTOR = HR.INSTRUTOR)
        WHERE  O.DISCIPLINA = 'Cálculo' -- AND O.PRECO_BASE > 0.00 AND O.PRECO_BASE < 100.00
            AND L.CIDADE = 'São Carlos' AND L.UF = 'SP' 
            AND HR.DIA_SEMANA = 'SEG' AND HR.HORARIO = '14:00'
    
    -- Sobre:: Precisa do distinct pq caso o usuário cadastre multiplos locais com o mesmo 
    -- par (cidade, uf) o mesmo instrutor é retornado diversas vezes.
    -- 
    -- Melhoria: Separar o relacionamento Local em Local,Espaço
    -- Local  -> Cidade, UF.
    -- Espaço -> Cidade, UF, Nome, rua, número, complemento, bairro.

-- 2) Selecionar, para cada turma existente na base de dados, a quantidade total de propostas
-- FINALIZADAS ou APROVADAS cujo preço total das aulas foi superior ou igual à R$ 100.00.

    SELECT T.NOME, COUNT(P.ID) QUANTIDADE
        FROM turma T
		LEFT JOIN proposta P ON (T.NOME = P.TURMA)
        WHERE (P.ID IS NULL) 
			OR (P.PRECO_TOTAL >= 100.00 AND P.STATUS IN ('FINALIZADA','APROVADA'))
		GROUP BY T.NOME
    -- Sobre:: Utilizando WHERE com OR para garantir que a seleção não exclua
    -- as turmas que não possuem proposta que cumprem os requisitos.

    SELECT T.NOME, COUNT(P.ID) QUANTIDADE
        FROM turma T
		LEFT JOIN ( SELECT P.ID, P.TURMA
				FROM PROPOSTA P
				WHERE P.PRECO_TOTAL >= 100.00 AND P.STATUS IN ('FINALIZADA','APROVADA')
			) P ON (T.NOME = P.TURMA)
		GROUP BY T.NOME;
    -- Sobre: Utilizando Sub-Queries para filtrar as propostas e remover a necessidade
    -- de utilizar o WHERE (P.ID IS NULL).

    -- Utiilizando EXPLAIN para verificar a eficiencia. Em ambos os casos há a necessidade de
    -- realizar uma busca sequencial tanto em turma quanto em proposta. No entanto, na segunda 
    -- versão o filtro das propostas é aplicado antes da junção e isso minimiza o custo da 
    -- LEFT JOIN (além de removar o custo da operação (P.ID IS NULL) presente na primeira versão)


-- 3) Retorne a quantide de horas que cada instrutor do sistema deu de aula nos últimos 30 dias.

    SELECT P.INSTRUTOR, SUM(A.DATA_FIM - A.DATA_INICIO)  -- A.PROPOSTA, A.DATA_INICIO, A.DATA_FIM, (A.DATA_FIM - A.DATA_INICIO) DURACAO --   DATE_PART('hour', A.DATA_INICIO - A.DATA_FIM) 'DURACAO'
        FROM aula A
        INNER JOIN proposta P ON (A.PROPOSTA = P.ID)
        WHERE A.STATUS = 'FINALIZADA' 
            AND A.DATA_INICIO >= ('now'::timestamp - '1 month'::interval)
        GROUP BY P.INSTRUTOR;
    -- Sobre: O Postgresql possui o sistema de subtração entre datas e intervalos 
    -- que tornaram a query mais limpa e simples do que eu esperava.

-- 4) Retornar o username e o score dos 10 instrutores com a maior média de avaliação na plataforma. 
-- Em caso de empate o desempate  deve ser feito pela quantidade de aulas dadas.
    
    SELECT A.INSTRUTOR, ROUND(AVG(AP.NOTA), 2) SCORE, COUNT(DISTINCT ROW(A.PROPOSTA, A.NUMERO)) QTD
        FROM aula A
        INNER JOIN avaliacao_participante AP ON (A.PROPOSTA = AP.PROPOSTA AND A.NUMERO = AP.NUMERO)
        GROUP BY A.INSTRUTOR 
        ORDER BY SCORE DESC, QTD DESC
        LIMIT 10
    -- Sobre: O fato da chave primária de aula ser composta aumentou um pouco o custo do
    -- desempate devido ao fato de ser necessário realizar um DISTINCT.
    -- 
    -- Obs: Seria interessante criar uma função para beneficiar o score de usuários com maior quantidade
    -- de aulas e evitar que novos instrutores ficassem com score 5 logo na primeira avaliação.

-- 5) Para alunos que já tiveram ao menos 1 aula realizada, buscar o username do instrutor com  
-- o qual ele teve mais aulas e a quantidade. Em caso de empate retornar qualquer um dos resultados.

    -- 1º Retorna a quantidade de aulas que um aluno teve com cada instrutor em ordem crescente
    SELECT  AC.ALUNO, A.INSTRUTOR, COUNT(*) COUNT
        FROM ACEITA AC 
        INNER JOIN aula A ON (AC.PROPOSTA = A.PROPOSTA)
        WHERE A.STATUS = 'FINALIZADA'
        GROUP BY AC.ALUNO, A.INSTRUTOR
        ORDER BY COUNT DESC

    -- 2º Reagrupa os usuários e pega o primeiro
    SELECT T.ALUNO, (array_agg(T.INSTRUTOR ORDER BY T.COUNT DESC))[1], MAX(T.COUNT) 
        FROM 
            ( SELECT  AC.ALUNO, A.INSTRUTOR, COUNT(*) COUNT
                FROM ACEITA AC 
                INNER JOIN aula A ON (AC.PROPOSTA = A.PROPOSTA)
                WHERE A.STATUS = 'FINALIZADA'
                GROUP BY AC.ALUNO, A.INSTRUTOR
                ORDER BY COUNT DESC ) AS T
        GROUP BY T.ALUNO;
    -- Sobre: Infelizmente em casos que há o agrupamento de 2 ou mais níveis, o SQL não possui 
    -- (ou pelo menos não é fácil achar), uma função que filtre apenas os subgrupos com a maior
    -- quantidade de linhas. Portanto é necessário fazer uma query aninhada para, em seguida, 
    -- reagrupar os resultados dos alunos utilizando uma função de agregação que exibe os
    -- instrutores em um array e, então, acessar o primeiro elemento.


-- 6) Para cada recomendação salva no banco, retornar quantas aulas o aluno responsável pela 
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


-------------------------------------------------------------------------------
-- ESTUDO DO FUNCIONAMENTO DA DIVISAO
SELECT * 
    FROM R 
    WHERE x not in ( 
        SELECT x FROM (
            (SELECT x , y 
                    FROM (select y from S) as p 
                    CROSS JOIN (select distinct x from R) as sp )
            EXCEPT 
            (SELECT x , y FROM R) 
        )  AS r 
    ); 




SELECT O.INSTRUTOR
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



 R(x,y) / S(y) = R(x)

R(x,y)      S(y)        Resultado Esperado
 A  1       1           A
 A  2       2           
 A  3       3
 B  1

(R(x) CROSS S(y))
A 1
A 2 
A 3
B 1
B 2
B 3 

(R(x) CROSS S(y)) MINUS (R(x))
A 1
A 2
A 3
B 1

R(x,y) tal que x not in (R(x) CROSS S(y)) MINUS (R(x))
B 2 
B 3

Extrai X vira: 
B 
B

