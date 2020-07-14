from src.dao.connector import Connector
from src.entities.class_ import Class

class ClassDAO(Connector):

    def __init__(self):
        super().__init__()

    def insert(self, class_:Class):
        try: 
            self.connect()
            query = '''INSERT INTO turma (NOME, TITULO, DESCRICAO, QTD_PARTICIAPNTES, MAX_PARTICIPANTES, SITUACAO)
                        VALUES (%s, %s, %s, %s, %s, %s);'''

            self.cur.execute(query, [class_.classname, class_.title, class_.description, class_.members_qtt, class_.max_members, class_.situation])
            self.con.commit()

        except Exception as e:
            print('[classDAO.insert]', str(e))
            raise Exception('fail on class registration. Check again later!')

        finally:
            self.close()

    def update(self):
        return True

    def select(self):
        return True