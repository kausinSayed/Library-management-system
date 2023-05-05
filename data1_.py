import sqlite3

def DataBase():
    con = sqlite3.connect('data1_.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data1_(id INTEGER PRIMARY KEY AUTOINCREMENT ,BID TEXT,Bti TEXT,Bau TEXT,Dbd INTEGER)")
    con.commit()
    con.close()
    
def Add(BID,Bti,Bau,Dbd):
    con = sqlite3.connect('data1_.db')
    cur = con.cursor()
    cur.execute("INSERT INTO data1_ VALUES(NULL,?,?,?,?)",(BID,Bti,Bau,Dbd))
    con.commit()
    con.close()
    
def View():
    con = sqlite3.connect('data1_.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data1_")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def Delete(id):
    con = sqlite3.connect('data1_.db')
    cur = con.cursor()
    cur.execute("DELETE FROM data1_ WHERE id =? ",(id,))
    con.commit()
    con.close()
    
    
def SearchData(BID="",Bti="",Bau="",Dbd=""):
    con = sqlite3.connect('data1_.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data1_ where BID=? OR Bti=? OR Bau=? OR Dbd=?",(BID,Bti,Bau,Dbd))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows    
    
    

def Update():
    con = sqlite3.connect('data1_.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data1_")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows
        
    
DataBase()