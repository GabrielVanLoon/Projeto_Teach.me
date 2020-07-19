from src.dao.connector     import Connector
from src.entities.proposal import Proposal

class ProposalDAO(Connector):
    
    def __init__(self):
        super().__init__()

    def insert(self, proposal:Proposal):
        try: 
            self.connect()
            query = '''INSERT INTO proposta (ID, TURMA, INSTRUTOR, DISCIPLINA, CODIGO, STATUS, DATA_CRIACAO, PRECO_TOTAL)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''

            self.cur.execute(query, [proposal.id, proposal.classname, proposal.instructor, proposal.subject, proposal.code, 
                                        proposal.status, proposal.creation_date, proposal.full_price])
            self.con.commit()

        except Exception as e:
            print('[proposalDAO.insert]', str(e))
            raise Exception('fail on proposal registration. Check again later!')

        finally:
            self.close()

    def update(self, proposal:Proposal):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE proposta 
                        SET STATUS = %s, DATA_CRIACAO = %s, PRECO_TOTAL = %s
                        WHERE TURMA = %s AND INSTRUTOR = %s AND DISCIPLINA = %s AND CODIGO = %s;'''

            self.cur.execute(query, [proposal.status, proposal.creation_date, proposal.full_price, 
                                        proposal.classname, proposal.instructor, proposal.subject, proposal.code])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[proposalDAO.update]', str(e))
            raise Exception('fail on proposal update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select(self, proposal:Proposal):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT ID, TURMA, INSTRUTOR, DISCIPLINA, CODIGO, STATUS, DATA_CRIACAO, PRECO_TOTAL
                        FROM proposta
                        WHERE TURMA = %s AND INSTRUTOR = %s AND DISCIPLINA = %s AND CODIGO = %s LIMIT 1;'''

            self.cur.execute(query, [proposal.classname, proposal.instructor, proposal.subject, proposal.code])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = Proposal(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])

        except Exception as e:
            print('[proposalDAO.select]', str(e))
            raise Exception('fail on proposal select. Check again later!')

        finally:
            self.close()

        return return_obj

    def update_by_id(self, proposal:Proposal):
        rows_affected = 0
        try: 
            self.connect()
            query = '''UPDATE proposta 
                        SET STATUS = %s, DATA_CRIACAO = %s, PRECO_TOTAL = %s
                        WHERE ID = %s;'''

            self.cur.execute(query, [proposal.status, proposal.creation_date, proposal.full_price, proposal.id])
            self.con.commit()
            
            rows_affected = self.cur.rowcount

        except Exception as e:
            print('[proposalDAO.update]', str(e))
            raise Exception('fail on proposal update. Check again later!')

        finally:
            self.close()

        return rows_affected

    def select_by_id(self, proposal:Proposal):
        return_obj = None
        try: 
            self.connect()
            query = '''SELECT ID, TURMA, INSTRUTOR, DISCIPLINA, CODIGO, STATUS, DATA_CRIACAO, PRECO_TOTAL
                        FROM proposta
                        WHERE ID = %s LIMIT 1;'''

            self.cur.execute(query, [proposal.id])
            self.con.commit()

            result = self.cur.fetchone()
            if (self.cur.rowcount == 1) and (result is not None):
                return_obj = Proposal(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])

        except Exception as e:
            print('[proposalDAO.select]', str(e))
            raise Exception('fail on proposal select. Check again later!')

        finally:
            self.close()

        return return_obj    

    def select_by_student(self, student:str, status:str = ''):
        return_obj = []
        n_rows     = 0

        try: 
            self.connect()
            query = '''SELECT P.ID, P.TURMA, P.INSTRUTOR, P.DISCIPLINA, P.CODIGO, P.STATUS, TO_CHAR(P.DATA_CRIACAO:: DATE, 'dd/mm/yyyy'), P.PRECO_TOTAL,
                                A.NUMERO, A.LOCAL, A.STATUS, A.PRECO_FINAL, TO_CHAR(A.DATA_INICIO:: DATE, 'dd/mm/yyyy hh:mm') ,   (AC.ALUNO IS NULL) ACEITO
                        FROM proposta P
                        INNER JOIN aula A ON (P.ID = A.PROPOSTA)
                        INNER JOIN participante PA ON (P.TURMA = PA.TURMA)
                        LEFT JOIN  aceita AC ON (P.ID = AC.PROPOSTA AND PA.ALUNO = AC.ALUNO AND PA.TURMA = AC.TURMA)
                        WHERE PA.ALUNO = %s'''

            if (status != ''):
                query += ''' AND P.STATUS = %s'''
                self.cur.execute(query, [student, status])
            else :
                self.cur.execute(query, [student])

            self.con.commit()

            return_obj  = self.cur.fetchall()
            n_rows      = self.cur.rowcount

        except Exception as e:
            print('[proposalDAO.select_by_student]', str(e))
            raise Exception('fail on proposal select. Check again later!')

        finally:
            self.close()

        return (n_rows, return_obj)   