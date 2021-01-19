import sqlite3
#backend

def studentData():
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, stdAd text, \
        firstname text, surname text, DoB text, Age text, Gender text, Parents_Contact text, Address text)")
    con.commit()
    con.close()

def addStudentRecord(stdAd, firstname, surname, DoB, Age , Gender, Parents_Contact, Address):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)",\
        (stdAd, firstname, surname, DoB, Age , Gender, Parents_Contact, Address))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM student")
    rows =cur.fetchall()
    con.close
    return rows

def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close
    
def searchData(stdAd="", firstname="", surname="", DoB="", Age="", Gender="", Parents_Contact="", Address=""):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM student WHERE stdAd=? OR firstname=? OR surname=? OR DoB=? OR Age=? OR Gender=? OR Parents_Contact=? OR \
            Address=? ", \
            (stdAd, firstname, surname, DoB, Age , Gender, Parents_Contact, Address))
    rows =cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,stdAd="", firstname="", surname="", DoB="", Age="", Gender="", Parents_Contact="", Address=""):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("UPDATE student SET stdAd=?, firstname=?, surname=?, DoB=?, Age=?, Gender=?, Parents_Contact=?, Address=?, WHERE id=?", \
        (stdAd, firstname, surname, DoB, Age , Gender, Parents_Contact, Address, id))
    con.commit()
    con.close()

studentData()