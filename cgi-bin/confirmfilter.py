#! /usr/bin/env python

import cgi
import cgitb
import os
import sqlite3
import shutil
cgitb.enable()
form = cgi.FieldStorage()
header = "Content-type: text/html\n\n"
mode = form.getvalue("mode")
loginid = form.getvalue("user")
filename = form.getvalue("filename")
db= sqlite3.connect("photo.db")
cursor=db.cursor()
cursor.execute("INSERT INTO photos (filename, user, mode) VALUES(?,?,?)",(filename,loginid,mode))
db.commit()
htmlhead = """
<!DOCTYPE html>
<html lang="en">
<head>
Confirm Changes
</head>
<body>"""


htmlmid="""<form method='POST' action='index.py'>
Image Saved!
<input type="hidden" name="user" value=%s></input>
<input type='submit' value='Back to Index'></input>
</form>"""%loginid

htmlbottom="""

</body>
</html>
"""
print (header + htmlhead)
print (htmlmid)
print (htmlbottom)
db.close()
