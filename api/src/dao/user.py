from src.dao.connector import Connector
from src.entities.user import User

class UserDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, user:User):
        try: 
            self.connect()
            query = '''INSERT INTO usuario (NOME_USUARIO, EMAIL, SENHA, NOME, SOBRENOME, E_INSTRUTOR)
                        VALUES (%s, %s, %s, %s, %s, %s);'''

            self.cur.execute(query, [user.username, user.email, user.password, user.name, user.last_name, user.is_instructor])
            self.con.commit()

        except Exception as e:
            print('[userDAO.insert]', str(e))
            raise Exception('fail on user registration. Check again later!')

        finally:
            self.close()

    def update(self):
        return True

    def select(self):
        return True
    