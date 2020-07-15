from src.dao.connector import Connector
from src.entities.place import Place

class PlaceDAO(Connector):

    def __init__(self):
        super().__init__()

    def insert(self, place:Place):
        try: 
            self.connect()
            query = '''INSERT INTO local (INSTRUTOR, NOME, CAPACIDADE, RUA, NUMERO, BAIRRO, COMPLEMENTO, CIDADE, UF)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'''

            self.cur.execute(query, [place.instructor, place.placename, place.capacity, place.street, place.number, place.neighborhood, place.complement, place.city, place.federal_state])
            self.con.commit()

        except Exception as e:
            print('[placeDAO.insert]', str(e))
            raise Exception('fail on place registration. Check again later!')

        finally:
            self.close()

    def update(self, place:Place):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE local 
                        SET CAPACIDADE = %s, RUA = %s, NUMERO = %s, BAIRRO = %s, COMPLEMENTO = %s, CIDADE = %s, UF = %s;'''

            self.cur.execute(query, [place.capacity, place.street, place.number, place.neighborhood, place.complement, place.city, place.federal_state])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[placeDAO.update]', str(e))
            raise Exception('fail on place update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, place:Place):
        return_place = None
        try: 
            self.connect()
            query = '''SELECT NOME, CAPACIDADE, RUA, NUMERO, BAIRRO, COMPLEMENTO, CIDADE, UF
                        FROM local 
                        WHERE INSTRUTOR = %s AND NOME = %s LIMIT 1;'''

            self.cur.execute(query, [place.instructor, place.placename])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_place = Place(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])

        except Exception as e:
            print('[placeDAO.select]', str(e))
            raise Exception('fail on place select. Check again later!')

        finally:
            self.close()

        return return_place