from src.dao.connector   import Connector
from src.entities.instructor import Instructor

class InstructorDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, instructor:Instructor):
        try: 
            self.connect()
            query = '''INSERT INTO instrutor (NOME_USUARIO, RESUMO, SOBRE_MIM, FORMACAO)
                        VALUES (%s, %s, %s, %s);'''

            self.cur.execute(query, [instructor.username, instructor.abstract, instructor.about_me, instructor.degree])
            self.con.commit()

        except Exception as e:
            print('[instructorDAO.insert]', str(e))
            raise Exception('fail on instructor registration. Check again later!')

        finally:
            self.close()

    def update(self, instructor:Instructor):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE instrutor 
                        SET RESUMO = %s, SOBRE_MIM = %s, FORMACAO = %s
                        WHERE NOME_USUARIO = %s;'''

            self.cur.execute(query, [instructor.abstract, instructor.about_me, instructor.degree, instructor.username])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[instructorDAO.update]', str(e))
            raise Exception('fail on instructor update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, instructor:Instructor):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT NOME_USUARIO, RESUMO, SOBRE_MIM, FORMACAO
                        FROM instrutor
                        WHERE NOME_USUARIO = %s LIMIT 1;'''

            self.cur.execute(query, [instructor.username])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = Instructor(result[0], result[1], result[2], result[3])

        except Exception as e:
            print('[instructorDAO.select]', str(e))
            raise Exception('fail on instructor select. Check again later!')

        finally:
            self.close()

        return return_obj

    def get_instructors(self, subject='', city='', state='', weekday='', time='', max_price=''):
        n_rows = 0
        result = []
        parameters = []
        try: 
            self.connect()

            # Montando as colunas: 
            query =  ''' SELECT DISTINCT ON (U.NOME_USUARIO) 
                            U.NOME_USUARIO, U.NOME, U.SOBRENOME, I.FORMACAO, I.RESUMO,  '''
            query += " O.DISCIPLINA, O.PRECO_BASE" if (subject != '') else " '', O.PRECO_BASE "

            # Joins obrigatórios:
            query += ''' FROM oferecimento O
                            INNER JOIN usuario U ON (O.INSTRUTOR = U.NOME_USUARIO)
                            INNER JOIN instrutor I ON (O.INSTRUTOR = I.NOME_USUARIO) '''

            # Joins opcionais
            if (state != ''):
                query += ''' INNER JOIN local L ON (O.INSTRUTOR = L.INSTRUTOR) '''

            if (weekday != '') or (time != ''):
                query += ''' INNER JOIN horario_disponivel HR ON (O.INSTRUTOR = HR.INSTRUTOR) '''
            

            # Montando a clausura Where baseada nos parâmetros
            if (subject != '') or (state != '') or (weekday != '') or (time != '') or (max_price != ''):
                query += ' WHERE'
                if (subject != ''):
                    query += ' O.DISCIPLINA = %s'
                    parameters.append(subject)
                
                if (state != ''):
                    if parameters:
                        query += ' AND'
                    query += ' L.UF = %s'
                    parameters.append(state)
                    if (city != ''):
                        query += ' AND L.CIDADE = %s'
                        parameters.append(city)
                
                if (weekday != ''):
                    if parameters:
                        query += ' AND'
                    query += ' HR.DIA_SEMANA = %s'
                    parameters.append(weekday)
                
                if (time != ''):
                    if parameters:
                        query += ' AND'
                    query += ' HR.HORARIO = %s'
                    parameters.append(time)

                if (max_price != ''):
                    if parameters:
                        query += ' AND'
                    query += ' O.PRECO_BASE <= %s'
                    parameters.append(max_price)
                
            query += ' ORDER BY U.NOME_USUARIO ASC, O.PRECO_BASE ASC;'
                

            self.cur.execute(query, parameters)
            self.con.commit()

            result = self.cur.fetchall()
            n_rows = self.cur.rowcount
            
        except Exception as e:
            print('[instructorDAO.select]', str(e))
            raise Exception('fail on instructor select. Check again later!')

        finally:
            self.close()
    
        return n_rows, result