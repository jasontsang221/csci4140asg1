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
def changepw(loginid,password):
    cursor.execute("UPDATE userinfo SET pw=? WHERE name=?",(password,loginid))
userid=form.getvalue("user")
pw=form.getvalue("pw")
currentpw=form.getvalue("currentpw")
newpw=form.getvalue("newpass")
renewpw=form.getvalue("renewpass")

htmlhead = """
<!DOCTYPE html>
<html lang="en">
<head>
Confirm Changes
</head>
<body>"""
htmlbottom="""

</body>
</html>
"""

print (htmlhead)
if pw != currentpw:
    print("<H1>Error: Wrong Password.</H1>")
    print("""<form method='POST' action='homepage.py'>
    <input type='submit' value='Back'></input>
    </form>""")
elif newpw != renewpw:#check if username and pw correct
    print("<H1>Error: New password not match.</H1>")
    print("""<form method='POST' action='homepage.py'>
    <input type='submit' value='Back'></input>
    </form>""")
else:
    changepw(userid,newpw)
    print("<H1>Password Changed Successfully")
    print("""<form method='POST' action='index.py'>
    <input type="hidden" name="user" value=%s></input>
    <input type='submit' value='Proceed'></input>
    </form>"""%userid)
print(htmlbottom)
