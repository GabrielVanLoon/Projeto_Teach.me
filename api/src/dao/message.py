from src.dao.connector import Connector
from src.entities.message import Message

class MessageDAO(Connector):

    def __init__(self):
        super().__init__()

    def insert(self, message:Message):
        try: 
            self.connect()
            query = '''INSERT INTO messagem (TURMA, CODIGO, NUMERO, USUARIO, DATA_ENVIO, CONTEUDO)
                        VALUES (%s, %s, %s, %s, %s, %s);'''

            self.cur.execute(query, [message.classname, message.chat_code, message.message_number, message.username, message.date, message.content])
            self.con.commit()

            print('[messageDAO.insert]', str(e))
            raise Exception('fail on message registration. Check again later!')

        finally:
            self.close()

    def update(self, message:Message):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE mensagem
                        SET CONTEUDO = %s;'''

            self.cur.execute(query, [message.content])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[messageDAO.update]', str(e))
            raise Exception('fail on message update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, message:Message):
        return_message = None
        try: 
            self.connect()
            query = '''SELECT TURMA, USUARIO, DATA_ENVIO, CONTEUDO
                        FROM mensagem 
                        WHERE TURMA = %s AND CODIGO = %s AND NUMERO = %s LIMIT 1;'''

            self.cur.execute(query, [message.classname, message.chat_code, message.message_number])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_message = Message(result[0], result[1], result[2], result[3])

        except Exception as e:
            print('[messageDAO.select]', str(e))
            raise Exception('fail on message select. Check again later!')

        finally:
            self.close()

        return return_message