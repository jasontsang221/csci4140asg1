#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
cgitb.enable()


db= sqlite3.connect("photo.db")

def updatepageid(loginid):
    cursor=db.cursor()
    c=db.cursor()
    for row in cursor.execute("SELECT * FROM photos ORDER BY id DESC"):
            if row[3]=='private' and row[2]==loginid:
                c.execute("INSERT INTO userphotos (filename, user, mode) VALUES(?,?,?)",(row[1],row[2],row[3]))
            elif row[3]=='public':
                c.execute("INSERT INTO userphotos (filename, user, mode) VALUES(?,?,?)",(row[1],row[2],row[3]))

def showphotos(loginid,page):
    cursor=db.cursor()
    print("<p>")
    for row in cursor.execute("SELECT * FROM userphotos ORDER BY id ASC"):
        if page==int((row[0]-1)/8)+1:
            if row[3]=='private' and row[2]==loginid:
                print("<a href =/Photos/%s > <img src=/Photos/%s ></a><br>"%(row[1],row[1]))
                #print("id=",row[0],"<br>\n")
            if row[3]=='public':
                print("<a href =/Photos/%s > <img src=/Photos/%s ></a><br>"%(row[1],row[1]))
                #print("id=",row[0],"<br>\n")
    print("</p>")
def countphoto(loginid):
    cursor=db.cursor()
    c=db.cursor()
    for row in cursor.execute("SELECT * FROM userphotos ORDER BY id DESC"):
            return int(int(row[0]-1)/8)+1
    return 1
header = "Content-type: text/html\n\n"
page=1
cursor=db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS photos(id INTEGER PRIMARY KEY NOT NULL, filename TEXT, user TEXT, mode TEXT,pageid INTEGER)
''')
c=db.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS userphotos(id INTEGER PRIMARY KEY NOT NULL, filename TEXT, user TEXT, mode TEXT,pageid INTEGER)
''')
db.commit()

cursor=db.cursor()
params=("sample.jpg", "jason", "public", 0)
#cursor.execute("INSERT INTO photos (filename, user, mode,pageid) VALUES(?,?,?,?)",params)
db.commit()

form = cgi.FieldStorage()
filename=form.getvalue("filename")
if "discard" in form:
    try:
        os.remove(os.getcwd()+"/Photos/"+filename)
    except OSError:
        pass

loginid=form.getvalue("user")
htmlhead = """
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
    max-width: 200px;
    max-height: 200px;

}

img:hover {
    box-shadow: 0 0 2px 1px rgb(0, 150, 190);
}


</style>
INDEX PAGE
</head>
<body>
<form method="POST" action="homepage.py">
Current User: %s
<input type="submit" value="Log out"></input>
</form>"""%(loginid)
print (header + htmlhead)
updatepageid(loginid)
showphotos(loginid,page)
numofpage=countphoto(loginid)
htmlmid="""
<form method="POST" action="newpage1.py">
Current page: %d of %d<br>
<input type="submit" value="Next page"></input>
<input type="hidden" name="curpage" value=%d></input>
<input type="hidden" name="user" value=%s></input>
<input type="hidden" name="next" value=next></input>
</form>
<form method="POST" action="newpage1.py">
<input type="submit" value="Previous page"></input>
<input type="hidden" name="curpage" value=%d></input>
<input type="hidden" name="user" value=%s></input>
<input type="hidden" name="next" value=prev></input>
</form>"""%(page,numofpage,page,loginid,page,loginid)
print (htmlmid)
#print(page,numofpage,loginid)
htmltail='''
</body>
</html>'''

print("<hr>")
htmlupload='''
<form method="POST" action="upload.py" enctype="multipart/form-data">
<input type="radio" name= "mode" value="public">Public<br>
<input type="radio" name= "mode" value="private">Private<br>
<input type="hidden" name="user" value=%s></input>
<input type="file" name="filename" accept="image/gif, image/jpeg, image/png">
<input type="submit" value="Upload"></input>
</form>

'''%loginid



print(htmlupload)
print (htmltail)
db.close()
