#! /usr/bin/env python

import cgi
import cgitb
import os
import sqlite3
cgitb.enable()


header = "Content-type: text/html\n\n"
form = cgi.FieldStorage()
db= sqlite3.connect("mydb.db",isolation_level=None)

def printdb():
    cursor=db.cursor()
    print("<p>")
    for row in cursor.execute("SELECT * FROM userinfo"):
        print("Username=",row[0])
        print("Password=",row[1],"\n")
    print("<p>")

def checkuserexist(loginid):
    cursor=db.cursor()
    for row in cursor.execute("SELECT * FROM userinfo"):
        if loginid==row[0]:
            return True
    else: return False

def addnewuser(loginid, password):
    params=(loginid, password)
    cursor=db.cursor()
    cursor.execute("INSERT INTO userinfo (name, pw) VALUES(?,?)",params)
    db.commit()

db.execute("SELECT * from userinfo")
loginid=form.getvalue("user")
password=form.getvalue("pass")
repassword=form.getvalue("re-pass")
htmlhead = """
<!DOCTYPE html>
<html lang="en">
<head>
LOGIN PAGE
</head>
<body>"""
htmlbottom="""

</body>
</html>
"""

print (header + htmlhead)
if "user" not in form or "pass" not in form or "re-pass" not in form:
    print("<H1>Error: Please fill in all information.</H1>")
    print("""<form method='POST' action='newac.py'>
    <input type='submit' value='Back'></input>
    </form>""")
elif password != repassword:
    print("<H1>Error: Unmatch information.</H1>")
    print("""<form method='POST' action='newac.py'>
    <input type='submit' value='Back'></input>
    </form>""")
elif checkuserexist(loginid): #check if username exist in db
    print("<H1>Error: Username Unavailable.</H1>")
    print("""<form method='POST' action='newac.py'>
    <input type='submit' value='Back'></input>
    </form>""")
else: #register
    addnewuser(loginid,password)
    print("<H1>New user added.</H1>")
    print("""<form method="POST" action="login.py">
    <input type="hidden" name="user" value=%s></input>
    <input type="hidden" name="pass" value=%s></input>
     <input type="submit" value="Proceed"></input>
     </form>"""%(loginid,password))
    printdb()
print(htmlbottom)
