from src.dao.connector import Connector
from src.entities.lesson import Lesson

class LessonDAO(Connector):

    def __init__(self):
        super().__init__()

    def insert(self, lesson:Lesson):
        try: 
            self.connect()
            query = '''INSERT INTO aula (PROPOSTA, NUMERO, INSTRUTOR, LOCAL, PRECO_FINAL, STATUS, DATA_INICIO, DATA_FIM, NOTA_INSTRUTOR)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'''

            self.cur.execute(query, [lesson.proposal, lesson.lesson_number, lesson.instructor, lesson.place, lesson.full_price, lesson.status, lesson.start, lesson.end, lesson.instructor_rate])
            self.con.commit()

        except Exception as e:
            print('[lessonDAO.insert]', str(e))
            raise Exception('fail on lesson registration. Check again later!')

        finally:
            self.close()

    def update(self, lesson:Lesson):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE aula
                        SET PRECO_FINAL = %s, STATUS = %s, DATA_INICIO = %s, DATA_FIM = %s, NOTA_INSTRUTOR = %s;'''

            self.cur.execute(query, [lesson.full_price, lesson.status, lesson.start, lesson.end, lesson.instructor_rate])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[lessonDAO.update]', str(e))
            raise Exception('fail on lesson update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, lesson:Lesson):
        return_lesson = None
        try: 
            self.connect()
            query = '''SELECT INSTRUTOR, LOCAL, PRECO_FINAL, STATUS, DATA_INICIO, DATA_FIM, NOTA_INSTRUTOR
                        FROM aula 
                        WHERE PROPOSTA = %s AND NUMERO = %s LIMIT 1;'''

            self.cur.execute(query, [lesson.instructor, lesson.lessonname])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_lesson = Lesson(result[0], result[1], result[2], result[3], result[4], result[5], result[6])

        except Exception as e:
            print('[lessonDAO.select]', str(e))
            raise Exception('fail on lesson select. Check again later!')

        finally:
            self.close()

        return return_lesson