#! /usr/bin/env python

import cgi
import cgitb
import os
import sqlite3
import shutil
from PIL import ImageFilter
from PIL import ImageOps
from PIL import Image
from PIL import ImageEnhance
cgitb.enable()
form = cgi.FieldStorage()
filternum=form.getvalue("filternum")
mode = form.getvalue("mode")
loginid = form.getvalue("user")
filename = form.getvalue("filename")
newfilepath = os.getcwd()+"/Photos/"+"new_"+filename
file=open(newfilepath,"w")
shutil.copy2(os.getcwd()+"/Photos/"+filename,newfilepath)
im=Image.open(newfilepath)
lf=Image.open(os.getcwd()+"/lensflare.jpg")
im=im.convert("RGB")
lf=lf.convert("RGB")
width, height = im.size
lf=lf.crop((0,0,width,height))
if filternum=="Border":
    img=ImageOps.expand(im,border=100,fill='black')
elif filternum=="Black White":
    img=im.convert("L")
elif filternum=="Lomo":
    img=ImageEnhance.Contrast(im).enhance(2)
elif filternum =="Lens Flare":
    img=Image.blend(im,lf,0.4)
elif filternum=="Blur":
    img=im.filter(ImageFilter.BLUR)
img.save(newfilepath)

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
Upload PAGE<br>
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
<form method="POST" action="filter.py">
<input type='submit' name= "filternum" value=Undo></input>
<input type="hidden" name="filename" value=%s></input>
<input type="hidden" name="mode" value=%s></input>
<input type="hidden" name="user" value=%s></input>
</form>
<form method="POST" action="confirmfilter.py">
<input type="hidden" name="filename" value=%s></input>
<input type="hidden" name="mode" value=%s></input>
<input type="hidden" name="user" value=%s></input>
<input type='submit'  value=Confirm></input>
</form>
'''%("new_"+filename,"new_"+filename,filename,mode,loginid,filename,mode,loginid,"new_"+filename,mode,loginid)

print(htmlhead)
print(htmlmid)
print(filternum)
print(htmltail)
