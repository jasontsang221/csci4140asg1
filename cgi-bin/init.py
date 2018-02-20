#! /usr/bin/env python

import cgi
import cgitb
import os
import sqlite3
import shutil
cgitb.enable()
db= sqlite3.connect("mydb.db")
cursor=db.cursor()
cursor.execute('''
DROP TABLE IF EXISTS userinfo
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS userinfo(name TEXT, pw TEXT)
''')
db.commit()
db.close()
pt= sqlite3.connect("mydb.db")
cursor=pt.cursor()
cursor.execute('''
DROP TABLE IF EXISTS photos
''')
cursor.execute('''
DROP TABLE IF EXISTS userphotos
''')
pt.commit()
shutil.rmtree(os.getcwd()+"/Photos/")
header = "Content-type: text/html\n\n"
htmlhead = """
<!DOCTYPE html>
<html lang="en">
<head>
LOGIN PAGE
</head>
<body>"""
print (header + htmlhead)
htmltail="""  <form method="POST" action="homepage.py">
System Initialized!
<input type="submit" name="OK"></input>
</form>
</body>
</html>
"""
print (htmltail)
