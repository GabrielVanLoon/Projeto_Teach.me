from src.dao.connector   import Connector
from src.entities.offer import Offer

class OfferDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, offer:Offer):
        try: 
            self.connect()
            query = '''INSERT INTO oferecimento (INSTRUTOR, DISCIPLINA, PRECO_BASE, METODOLOGIA)
                        VALUES (%s, %s, %s, %s);'''

            self.cur.execute(query, [offer.instructor, offer.subject, offer.base_price, offer.methodology])
            self.con.commit()

        except Exception as e:
            print('[offerDAO.insert]', str(e))
            raise Exception('fail on offer registration. Check again later!')

        finally:
            self.close()

    def update(self, offer:Offer):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE oferecimento 
                        SET PRECO_BASE = %s, METODOLOGIA = %s
                        WHERE INSTRUTOR = %s AND DISCIPLINA = %s;'''

            self.cur.execute(query, [offer.base_price, offer.methodology, offer.instructor, offer.subject])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[offerDAO.update]', str(e))
            raise Exception('fail on offer update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, offer:Offer):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT INSTRUTOR, DISCIPLINA, PRECO_BASE, METODOLOGIA
                        FROM oferecimento
                        WHERE INSTRUTOR = %s AND DISCIPLINA = %s LIMIT 1;'''

            self.cur.execute(query, [offer.student, offer.study_class])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = offer(result[0], result[1], result[2], result[3])

        except Exception as e:
            print('[offerDAO.select]', str(e))
            raise Exception('fail on offer select. Check again later!')

        finally:
            self.close()

        return return_obj
    