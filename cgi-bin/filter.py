#! /usr/bin/env python

import cgi
import cgitb
import os
import sqlite3
cgitb.enable()
form = cgi.FieldStorage()
mode = form.getvalue("mode")
loginid = form.getvalue("user")
filename = form.getvalue("filename")
filternum=form.getvalue("filternum")
if filternum=="Undo":
    os.remove(os.getcwd()+"/Photos/"+"new_"+filename)
htmlhead='''
<!DOCTYPE html>
<html lang="en">
<head>
<style>
img {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 5px;
    height: auto;
    width: auto;
    max-width: 600px;
    max-height: 600px;
}
</style>
Add Filter<br>
</head>
<body>
'''
htmltail="""
</body>
</html>
"""
htmlmid='''
<a href =/Photos/%s > <img src=/Photos/%s ></a><br>
<form method="POST" action="applyfilter.py">
Select Filter:
<input type='submit' name= "filternum" value=Border></input>
<input type='submit' name= "filternum" value=Lomo></input>
<input type='submit' name= "filternum" value="Lens Flare"></input>
<input type='submit' name= "filternum" value="Black White"></input>
<input type='submit' name= "filternum" value=Blur></input>
<input type="hidden" name="filename" value=%s></input>
<input type="hidden" name="mode" value=%s></input>
<input type="hidden" name="user" value=%s></input>
</form>
<form method="POST" action="index.py">
<input type="hidden" name="filename" value=%s></input>
<input type="hidden" name="mode" value=%s></input>
<input type="hidden" name="user" value=%s></input>
<input type='submit' name= "discard" value="Discard"></input>
</form>
<form method="POST" action="confirmfilter.py">
<input type="hidden" name="filename" value=%s></input>
<input type="hidden" name="mode" value=%s></input>
<input type="hidden" name="user" value=%s></input>
<input type='submit'  value=Confirm></input>
</form>
'''%(filename,filename,filename,mode,loginid,filename,mode,loginid,filename,mode,loginid)

print(htmlhead)
print(htmlmid)
print(filename)
print(htmltail)
