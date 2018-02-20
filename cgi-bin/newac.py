#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
cgitb.enable()
db= sqlite3.connect("mydb.db")

header = "Content-type: text/html\n\n"


date_string = time.strftime('%A, %B %d, %Y at %I:%M:%S %p %Z')

htmlhead = """
<!DOCTYPE html>
<html lang="en">
<head>
New Account
</head>
<body>
  <form method="POST" action="accreg.py">
Username:
<input type="text" name="user"></input><br>
Password:
<input type="password" name="pass"></input><br>
Re-type Password:
<input type="password" name="re-pass"></input><br>
<input type="submit"></input>
</form>
<form method="POST" action="login.py">
<input type="submit" value="Back"></input>"""

htmltail = """
</form>
</body>
</html>
"""

print (header + htmlhead)

print(htmltail)
db.close()
