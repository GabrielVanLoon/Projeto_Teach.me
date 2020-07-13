#!/usr/bin/env python
import os
import sys  
import psycopg2     # Ref: https://www.psycopg.org/docs/

db_user = 'teachme_user'
db_pass = 'Th3Cl4ws0fW1nt3rSubV3RtTh3wEak'
db_name = 'teachme_db'
db_host = 'localhost'

def example_connection():
    con = None
    cur = None
    try:
        con = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
        cur = con.cursor()
        
        sql = 'CREATE TABLE IF NOT EXISTS test_psycopg2 (id serial primary key, nome varchar(100), uf varchar(2));'
        cur.execute(sql)

        con.commit()
        con.close()
    except Exception as e:
        print("' [x]  Erro: Ocorreu um erro em test_connection()")
        print(" [x]  Error message: ", str(e))
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def example_insertion():
    con = None
    cur = None
    try:
        con = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
        cur = con.cursor()
        
        sql = 'INSERT INTO test_psycopg2 VALUES (%s, %s, %s);'
        cur.execute(sql, (1, 'Gabriel', 'SP'))
        cur.execute(sql, (2, 'Bablibó', 'RJ'))

        con.commit()
    except Exception as e:
        print(" [x]  Erro: Ocorreu um erro em test_connection()")
        print(" [x]  Error message: ", str(e))
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def example_update(id = 1):
    con = None
    cur = None
    try:
        con = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
        cur = con.cursor()
        
        sql = 'UPDATE test_psycopg2 SET nome = %s WHERE id = %s'
        cur.execute(sql, ['Bob', id])
        print(' [B]  Linhas afetadas: ', cur.rowcount)

        con.commit()
    except Exception as e:
        print(" [x]  Erro: Ocorreu um erro em example_update()")
        print(" [x]  Error message: ", str(e))
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def example_select_all():
    con = None
    cur = None
    try:
        con = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
        cur = con.cursor()
        
        sql = 'SELECT * FROM test_psycopg2'
        cur.execute(sql)
        
        results = cur.fetchall() 
        print(' [B]  Results: ', str(results))
        print(' [B]  Linhas afetadas: ', cur.rowcount)
    except Exception as e:
        print(" [x]  Erro: Ocorreu um erro em example_select_all()")
        print(" [x]  Error message: ", str(e))
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def example_select(id = 1):
    con = None
    cur = None
    try:
        con = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
        cur = con.cursor()
        
        sql = 'SELECT * FROM test_psycopg2 WHERE id = %s'
        cur.execute(sql, [id])
        
        results = cur.fetchall() 
        print(' [B]  Results: ', str(results))
        print(' [B]  Linhas afetadas: ', cur.rowcount)
    except Exception as e:
        print(" [x]  Erro: Ocorreu um erro em example_select()")
        print(" [x]  Error message: ", str(e))
    finally:
        if con is not None:
            con.close()
        if cur is not None:
            cur.close()

def main():
    try: 
        print(' [+]  Teach.me Database + Psycopg2...')
        example_connection()
        example_insertion()
        example_update(1)
        example_update(33) 
        example_select_all()
        example_select(1)
        example_select(33)
    except:
        print(' [x]  Erro: falha no script. Abortando...')

if __name__ == '__main__':
    main()