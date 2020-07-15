from src.dao.connector import Connector
from src.entities.subject import Subject

class SubjectDAO(Connector):

    def __init__(self):
        super().__init__()

    def insert(self, subject:Subject):
        try: 
            self.connect()
            query = '''INSERT INTO disciplina (NOME, DISCIPLINA_PAI)
                        VALUES (%s, %s);'''

            self.cur.execute(query, [subject.name, subject.parent_subject])
            self.con.commit()

        except Exception as e:
            print('[subjectDAO.insert]', str(e))
            raise Exception('fail on subject registration. Check again later!')

        finally:
            self.close()

    def update(self, subject:Subject):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE disciplina 
                        SET DISCIPLINA_PAI %s;'''

            self.cur.execute(query, [subject.parent_subject])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[subjectDAO.update]', str(e))
            raise Exception('fail on subject update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, subject:Subject):
        return_subject = None
        try: 
            self.connect()
            query = '''SELECT NOME, DISCIPLINA_PAI
                        FROM disciplina 
                        WHERE NOME = %s LIMIT 1;'''

            self.cur.execute(query, [subject.name])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_subject = Subject(result[0], result[1])

        except Exception as e:
            print('[subjectDAO.select]', str(e))
            raise Exception('fail on subject select. Check again later!')

        finally:
            self.close()

        return return_subject