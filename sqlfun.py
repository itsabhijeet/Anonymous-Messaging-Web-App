import sqlite3 as sql

def checkUserName(uname,email,name):
    con = sql.connect("notsarahah.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (uname,))
    users = cur.fetchall()
    con.close()
    print(users)
    if len(users) == 0:
       print("No user with this username")        
       return True
    else:
       return False

def insertUser(uname,email,name):
    con = sql.connect("notsarahah.db")
    cur = con.cursor()
    cur.execute("INSERT into users (username,email,name) VALUES (?,?,?)",(uname,email,name))
    con.commit()
    con.close()
    print("Inserted")

def getName(uname):
    con = sql.connect("notsarahah.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT  name FROM users where username=?",(uname,))
    name = cur.fetchone()
    print(name['name'])
    con.close()   
    return name['name']

def getEmail(uname):
    con = sql.connect("notsarahah.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT email FROM users where username=?",(uname,))
    email = cur.fetchone()
    print(email['email'])
    con.close()   
    return email['email']