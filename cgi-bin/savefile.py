#! /usr/bin/env python

import cgi
import cgitb
import os
import sqlite3
cgitb.enable()


header = "Content-type: text/html\n\n"
form = cgi.FieldStorage()
db= sqlite3.connect("mydb.db",isolation_level=None)
db.execute("SELECT * from photos")
loginid=form.getvalue("user")
filename=form.getvalue("name")
mode=form.getvalue("mode")
#cursor.execute("INSERT INTO photos (filename, user, mode,pageid) VALUES(?,?,?,?)",params)

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
addnewuser(loginid,password)
print("<H1>New user added.</H1>")
print("""<form method='POST' action='index.py'>
<input type="hidden" name="user" value=%s></input>
<input type="hidden" name="pw" value=%s></input>
<input type='submit' value='Back to Index'></input>
</form>"""%(userid,password))

print(htmlbottom)
db.close()
