from src.dao.connector   import Connector
from src.entities.available_time import AvailableTime

class AvailableTimeDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, available_time:AvailableTime):
        try: 
            self.connect()
            query = '''INSERT INTO horario_disponivel (INSTRUTOR, DIA_SEMANA, HORARIO)
                        VALUES (%s, %s, %s);'''

            self.cur.execute(query, [available_time.instructor, available_time.weekday, available_time.time])
            self.con.commit()

        except Exception as e:
            print('[available_timeDAO.insert]', str(e))
            raise Exception('fail on available time registration. Check again later!')

        finally:
            self.close()

    def select(self, available_time:AvailableTime):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT INSTRUTOR, DIA_SEMANA, HORARIO
                        FROM horario_disponivel
                        WHERE INSTRUTOR = %s AND DIA_SEMANA = %s AND HORARIO = %s LIMIT 1;'''

            self.cur.execute(query, [available_time.instructor, available_time.weekday, available_time.time])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = available_time(result[0], result[1], result[2], result[3])

        except Exception as e:
            print('[available_timeDAO.select]', str(e))
            raise Exception('fail on available time select. Check again later!')

        finally:
            self.close()

        return return_obj
    