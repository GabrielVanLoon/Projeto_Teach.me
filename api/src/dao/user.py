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

    def update(self, user:User):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE usuario 
                        SET EMAIL = %s, NOME = %s, SOBRENOME = %s, E_INSTRUTOR = %s
                        WHERE NOME_USUARIO = %s;'''

            self.cur.execute(query, [user.email, user.name, user.last_name, user.is_instructor, user.username])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[userDAO.update]', str(e))
            raise Exception('fail on user update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, user:User):
        return_user = None
        try: 
            self.connect()
            query = '''SELECT NOME_USUARIO, EMAIL, NOME, SOBRENOME, FOTO, E_INSTRUTOR
                        FROM usuario 
                        WHERE NOME_USUARIO = %s LIMIT 1;'''

            self.cur.execute(query, [user.username])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_user = User(result[0], result[1], None, result[2], result[3], result[4], result[5])

        except Exception as e:
            print('[userDAO.select]', str(e))
            raise Exception('fail on user select. Check again later!')

        finally:
            self.close()

        return return_user

    def login(self, user:User):
        return_user = None
        try: 
            self.connect()
            query = '''SELECT NOME_USUARIO, EMAIL, NOME, SOBRENOME, E_INSTRUTOR
                        FROM usuario
                        WHERE NOME_USUARIO = %s AND SENHA = %s LIMIT 1;''' #OR EMAIL = %s AND SENHA = %s

            self.cur.execute(query, [user.username, user.password])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_user = User(result[0], result[1], None, result[2], result[3], None, result[4])

        except Exception as e:
            print('[userDAO.select]', str(e))
            raise Exception('fail on user select. Check again later!')

        finally:
            self.close()

        return return_user
    
    def check_username(self, user:User):

        try: 
            self.connect()
            query = '''SELECT NOME_USUARIO
                        FROM usuario
                        WHERE NOME_USUARIO = %s LIMIT 1
                        UNION 
                        SELECT NOME 
                        FROM turma T
                        WHERE T.NOME = %s LIMIT 1;'''

            self.cur.execute(query, [user.username, user.username])
            self.con.commit()

            result = self.cur.fetchone()
            rowcount = self.cur.rowcount
            self.close()
            if (self.cur.rowcount == 1) and (result is not None):
                return True
            return False

        except Exception as e:
            print('[userDAO.select]', str(e))
            raise Exception('fail on user select. Check again later!')
 