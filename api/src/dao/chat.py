from src.dao.connector   import Connector
from src.entities.chat import Chat

class ChatDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, chat:Chat):
        try: 
            self.connect()
            query = '''INSERT INTO chat (TURMA, NOME, STATUS, INSTRUTOR)
                        VALUES (%s, %s, %s, %s);'''

            self.cur.execute(query, [chat.classname, chat.name, chat.status, chat.instructor])
            self.con.commit()

        except Exception as e:
            print('[chatDAO.insert]', str(e))
            raise Exception('fail on chat registration. Check again later!')

        finally:
            self.close()

    def update(self, chat:Chat):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE INSTRUTOR 
                        SET NOME = %s, STATUS = %s
                        WHERE TURMA = %s AND CODIGO = %s;'''

            self.cur.execute(query, [chat.name, chat.status, chat.classname, chat.chat_code])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[chatDAO.update]', str(e))
            raise Exception('fail on chat update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, chat:Chat):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT TURMA, CODIGO, NOME, STATUS, INSTRUTOR
                        FROM chat
                        WHERE TURMA = %s AND CODIGO = %s LIMIT 1;'''

            self.cur.execute(query, [chat.classname, chat.chat_code])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = chat(result[0], result[1], result[2], result[3], result[4])

        except Exception as e:
            print('[chatDAO.select]', str(e))
            raise Exception('fail on chat select. Check again later!')

        finally:
            self.close()

        return return_obj
    