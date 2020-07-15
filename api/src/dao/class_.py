from src.dao.connector import Connector
from src.entities.class_ import Class

class ClassDAO(Connector):

    def __init__(self):
        super().__init__()

    def insert(self, class_:Class):
        try: 
            self.connect()
            query = '''INSERT INTO turma (NOME, TITULO, DESCRICAO, QTD_PARTICIPANTES, MAX_PARTICIPANTES, SITUACAO)
                        VALUES (%s, %s, %s, %s, %s, %s);'''

            self.cur.execute(query, [class_.classname, class_.title, class_.description, class_.members_qtt, class_.max_members, class_.situation])
            self.con.commit()

        except Exception as e:
            print('[classDAO.insert]', str(e))
            raise Exception('fail on class registration. Check again later!')

        finally:
            self.close()

    def update(self, class_:Class):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE turma 
                        SET TITULO = %s, DESCRICAO = %s, MAX_PARTICIPANTES = %s, SITUACAO = %s
                        WHERE NOME = %s;'''

            self.cur.execute(query, [class_.title, class_.description, class_.max_members, class_.situation])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[ClassDAO.update]', str(e))
            raise Exception('fail on class update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, class_:Class):
        return_class = None
        try: 
            self.connect()
            query = '''SELECT NOME, TITULO, DESCRICAO, IMAGEM, QTD_PARTICIPANTES, MAX_PARTICIPANTES, SITUACAO
                        FROM turma 
                        WHERE NOME = %s LIMIT 1;'''

            self.cur.execute(query, [class_.classname])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_class = Class(result[0], result[1], result[2], result[3], result[4], result[5], result[6])

        except Exception as e:
            print('[ClassDAO.select]', str(e))
            raise Exception('fail on class select. Check again later!')

        finally:
            self.close()

        return return_class