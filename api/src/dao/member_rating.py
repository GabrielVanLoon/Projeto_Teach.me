from src.dao.connector   import Connector
from src.entities.member_rating import MemberRating

class MemberRatingDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, member_rating:MemberRating):
        try: 
            self.connect()
            query = '''INSERT INTO avaliacao_participante (ALUNO, TURMA, PROPOSTA, NUMERO, NOTA)
                        VALUES (%s, %s, %s, %s, %s);'''

            self.cur.execute(query, [member_rating.student, member_rating.classname, member_rating.proposal, member_rating.lesson_number, member_rating.rate])
            self.con.commit()

        except Exception as e:
            print('[memberRatingDAO.insert]', str(e))
            raise Exception('fail on member rating registration. Check again later!')

        finally:
            self.close()

    def update(self, member_rating:MemberRating):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE avaliacao_participante 
                        SET NOTA = %s
                        WHERE ALUNO = %s AND TURMA = %s AND PROPOSTA = %s AND NUMERO = %s;'''

            self.cur.execute(query, [member_rating.rate, member_rating.student, member_rating.classname, member_rating.proposal, member_rating.lesson_number])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[memberRatingDAO.update]', str(e))
            raise Exception('fail on member rating update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, member_rating:MemberRating):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT ALUNO, TURMA, PROPOSTA, NUMERO, NOTA
                        FROM avaliacao_participante
                        WHERE ALUNO = %s AND TURMA = %s AND PROPOSTA = %s AND NUMERO = %s LIMIT 1;'''

            self.cur.execute(query, [member_rating.student, member_rating.classname, member_rating.proposal, member_rating.lesson_number])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = member_rating(result[0], result[1], result[2], result[3], result[4])

        except Exception as e:
            print('[memberRatingDAO.select]', str(e))
            raise Exception('fail on member rating select. Check again later!')

        finally:
            self.close()

        return return_obj
    