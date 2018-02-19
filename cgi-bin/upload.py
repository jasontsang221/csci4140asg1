#! /usr/bin/env python

import cgi
import cgitb
import os
import sqlite3
from PIL import Image
cgitb.enable()
form = cgi.FieldStorage()
mode = form.getvalue("mode")
loginid = form.getvalue("user")

fileItem = form["filename"]

header = "Content-type: text/html\n\n"


htmlhead = """
<!DOCTYPE html>
<html lang="en">
<head>
Confirm Upload
</head>
<body>"""
print (header + htmlhead)
print("<br>",fileItem.filename)
isImage=1

open(os.getcwd()+"/Photos/"+fileItem.filename, 'wb').write(fileItem.file.read())
if "mode" not in form:
    print("""<form method='POST' action='index.py'>
    Error: Please Select Mode!
    <input type="hidden" name="user" value=%s></input>
    <input type='submit' value='Back'></input>
    </form>"""%loginid)
    isImage=0
try:
    im=Image.open(os.getcwd()+"/Photos/"+fileItem.filename)
except IOError:
    print("""<form method='POST' action='index.py'>
    Error: Wrong File Type!
    <input type="hidden" name="user" value=%s></input>
    <input type='submit' value='Back'></input>
    </form>"""%loginid)
    isImage=0
if isImage==1:
    print("""<form method='POST' action='filter.py'>
    <input type="hidden" name="filename" value=%s></input>
    <input type="hidden" name="mode" value=%s></input>
    <input type="hidden" name="user" value=%s></input>
    <input type='submit' value='Next'></input>
    </form>"""%(fileItem.filename,mode,loginid))
htmltail="""
</body>
</html>
"""
print (htmltail)
