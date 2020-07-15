from src.dao.connector   import Connector
from src.entities.recommendation import Recommendation

class RecommendationDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, recommendation:Recommendation):
        try: 
            self.connect()
            query = '''INSERT INTO recomenda (ALUNO, INSTRUTOR, TEXTO)
                        VALUES (%s, %s, %s);'''

            self.cur.execute(query, [recommendation.student, recommendation.instructor, recommendation.text])
            self.con.commit()

        except Exception as e:
            print('[recommendationDAO.insert]', str(e))
            raise Exception('fail on recommendation registration. Check again later!')

        finally:
            self.close()

    def update(self, recommendation:Recommendation):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE recomenda 
                        SET TEXTO = %s
                        WHERE ALUNO = %s AND INSTRUTOR = %s'''

            self.cur.execute(query, [recommendation.text, recommendation.student, recommendation.instructor])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[recommendationDAO.update]', str(e))
            raise Exception('fail on recommendation update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, recommendation:Recommendation):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT ALUNO, INSTRUTOR, TEXTO
                        FROM recomenda
                        WHERE ALUNO = %s AND INSTRUTOR = %s LIMIT 1;'''

            self.cur.execute(query, [recommendation.student, recommendation.instructor])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = recommendation(result[0], result[1], result[2])

        except Exception as e:
            print('[recommendationDAO.select]', str(e))
            raise Exception('fail on recommendation select. Check again later!')

        finally:
            self.close()

        return return_obj
    