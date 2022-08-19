import sqlite3
def create_pharmacy_db():
    con=sqlite3.connect(database=r'python.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pharmacy(ref  INTEGER PRIMARY KEY AUTOINCREMENT ,companyname  text,type  text,tabletname  text,lotno  text,issuedate  text,expdate  text,uses  text,sideeffect  text,warning  text,dosage  text,price  text,productqty  text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS pharma(ref INTEGER PRIMARY KEY AUTOINCREMENT ,medname text)")

    con.commit()

    
        


create_pharmacy_db()    