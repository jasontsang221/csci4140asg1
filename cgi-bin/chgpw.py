#! /usr/bin/env python

import cgi
import cgitb
import time
import os
cgitb.enable()

form = cgi.FieldStorage()

loginid=form.getvalue("user")
password=form.getvalue("pw")
header = "Content-type: text/html\n\n"



html = """
<!DOCTYPE html>
<html lang="en">
<head>
Change Password
</head>
<body>
  <form method="POST" action="confirmpwchg.py">
Current Password:
<input type="text" name="currentpw"></input><br>
New Password:
<input type="password" name="newpass"></input><br>
Re-type Password:
<input type="password" name="renewpass"></input><br>
<input type="submit" value="Go"></input>
<input type="hidden" name="user" value=%s></input><br>
<input type="hidden" name="pw" value=%s></input><br>
</form>
</body>
</html>
"""%(loginid,password)

print (header + html)
