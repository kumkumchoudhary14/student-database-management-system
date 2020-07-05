import sqlite3
#backend

def studentData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY ,StdID text,Firstname text,Surname text,DoB text,Age text,Address text,Mobile text,\
                       Gender text)")
    con.commit()
    con.close()

def addStdRec(StdID,Firstname,Surname,DoB,Age,Address,Mobile,Gender):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",\
                (StdID,Firstname,Surname,DoB,Age,Address,Mobile,Gender))
    con.commit()
    con.close()




def viewData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close

def searchData(id,StdID="",Firstname="",Surname="",DoB="",Age="",Address="",Mobile="",Gender=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT* FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Address=? OR Mobile=? OR Gender=?",(StdID,Firstname,Surname,DoB,Age,Address,Mobile,Gender, id))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,StdID="",Firstname="",Surname="",DoB="",Age="",Address="",Mobile="",Gender=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Address=? OR Mobile=? OR Gender=?",(StdID,Firstname,Surname,DoB,Age,Address,Mobile,Gender, id))
    con.commit()
    con.close()

studentData()
    
