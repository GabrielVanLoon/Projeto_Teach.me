from src.dao.connector   import Connector
from src.entities.accepts import Accepts

class AcceptsDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, accepts:Accepts):
        try: 
            self.connect()
            query = '''INSERT INTO aceita (ALUNO, TURMA, PROPOSTA)
                        VALUES (%s, %s, %s);'''

            self.cur.execute(query, [accepts.student, accepts.classname, accepts.proposal])
            self.con.commit()

        except Exception as e:
            print('[acceptsDAO.insert]', str(e))
            raise Exception('fail on accepts registration. Check again later!')

        finally:
            self.close()

    def select(self, accepts:Accepts):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT ALUNO, TURMA, PROPOSTA
                        FROM aceita
                        WHERE ALUNO = %s AND TURMA = %s AND PROPOSTA = %s LIMIT 1;'''

            self.cur.execute(query, [accepts.student, accepts.classname, accepts.proposal])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = accepts(result[0], result[1], result[2])

        except Exception as e:
            print('[acceptsDAO.select]', str(e))
            raise Exception('fail on accepts select. Check again later!')

        finally:
            self.close()

        return return_obj