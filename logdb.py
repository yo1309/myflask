import sqlite3

def dbcon():
    return sqlite3.connect('hello_db.db')

def create_table(): 
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE member (num varchar(50), name varchar(50))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(id, pw):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw)
        c.execute("INSERT INTO member VALUES(?,?)", setdata)
        db.commit()
    except Exception as e:
        print('db error', e)
    finally:
        db.close()
    
def select_all(): 
    ret = list() 
    try: 
        db = dbcon() 
        c = db.cursor() 
        c.execute('SELECT * FROM member') 
        ret = c.fetchall() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
        return ret




