import psycopg2     # Ref: https://www.psycopg.org/docs/

class Connector:
    def __init__(self):
        self.db_username = 'teachme_user'
        self.db_password = 'Th3Cl4ws0fW1nt3rSubV3RtTh3wEak'
        self.db_name = 'teachme_db'
        self.db_host = 'localhost'
        self.con = None
        self.cur  = None

    def connect(self):
        if (self.cur != None) or (self.con != None):
            self.close() 
        try: 
            self.cur = self.con = None 
            self.con = psycopg2.connect(host = self.db_host, database = self.db_name, 
                                    user = self.db_username, password = self.db_password)
            self.cur = self.con.cursor()
        except:
            raise

    def close(self):
        if self.con is not None:
            self.con.close()
        if self.cur is not None:
            self.cur.close()



