#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
cgitb.enable()


header = "Content-type: text/html\n\n"
db= sqlite3.connect("mydb.db")
cursor=db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS userinfo(name TEXT, pw TEXT)
''')
db.commit()
params=("admin", "admin")
cursor.execute("INSERT INTO userinfo (name, pw) VALUES(?,?)",params)
db.commit()
htmlhead = """
<!DOCTYPE html>
<html lang="en">
<head>
LOGIN PAGE
</head>
<body>"""
print (header + htmlhead)

htmltail="""  <form method="POST" action="login.py">
Username:
<input type="text" name="user"></input><br>
Password:
<input type="password" name="pass"></input><br>
<input type="submit"></input>
</form>
<form method="POST" action="newac.py">
<input type="submit" value="New Account"></input>
</form>
</body>
</html>
"""
print (htmltail)
db.close()
