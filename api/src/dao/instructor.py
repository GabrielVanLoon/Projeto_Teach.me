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
    