from src.dao.connector   import Connector
from src.entities.member import Member

class MemberDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, member:Member):
        try: 
            self.connect()
            query = '''INSERT INTO participante (ALUNO, TURMA, E_LIDER)
                        VALUES (%s, %s, %s);'''

            self.cur.execute(query, [member.student, member.study_class, member.is_leader])
            self.con.commit()

        except Exception as e:
            print('[memberDAO.insert]', str(e))
            raise Exception('fail on member registration. Check again later!')

        finally:
            self.close()

    def update(self, member:Member):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE participante 
                        SET E_LIDER = %s
                        WHERE ALUNO = %s AND TURMA = %s;'''

            self.cur.execute(query, [member.is_leader, member.student, member.study_class])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[memberDAO.update]', str(e))
            raise Exception('fail on member update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, member:Member):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT ALUNO, TURMA, E_LIDER
                        FROM participante 
                        WHERE ALUNO = %s AND TURMA = %s LIMIT 1;'''

            self.cur.execute(query, [member.student, member.study_class])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = Member(result[0], result[1], result[2])

        except Exception as e:
            print('[memberDAO.select]', str(e))
            raise Exception('fail on member select. Check again later!')

        finally:
            self.close()

        return return_obj
    