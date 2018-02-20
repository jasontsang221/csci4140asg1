#! /usr/bin/env python

import cgi
import cgitb
import os
import sqlite3
cgitb.enable()


header = "Content-type: text/html\n\n"
form = cgi.FieldStorage()
db= sqlite3.connect("mydb.db")
cursor=db.cursor()
db.execute("SELECT * from userinfo")
def checkuserexist(loginid,password):
    for row in cursor.execute("SELECT * FROM userinfo"):
        if loginid==row[0]:
            if password==row[1]:
                return True
            else: return False

password=form.getvalue("pass")
userid=form.getvalue("user")
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

print (htmlhead)
if "user" not in form or "pass" not in form:# Missing Info
    print("<H1>Error: Please fill in all information.</H1>")
    print("""<form method='POST' action='homepage.py'>
    <input type='submit' value='Back'></input>
    </form>""")
elif checkuserexist(userid, password):#Correct Login Info
    print("""<form method='POST' action='chgpw.py'>
    <p>Do you want to change password?</p>
    <input type="hidden" name="user" value=%s></input>
    <input type="hidden" name="pw" value=%s></input>
    <input type='submit' value='Yes'></input>
    </form>"""%(userid,password))
    print("""<form method='POST' action='index.py'>
    <input type="hidden" name="user" value=%s></input>
    <input type="hidden" name="pw" value=%s></input>
    <input type='submit' value='No'></input>
    </form>"""%(userid,password))
else:#incorrect pw
    print("<H1>Error: Username/Password is incorrect.</H1>")
    print("""<form method='POST' action='homepage.py'>
    <input type='submit' value='Back'></input>
    </form>""")
print(htmlbottom)
db.close()
