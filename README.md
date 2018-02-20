# csci4140asg1

Link to website on OpenShift server: http://webig-csci4140instagram.a3c1.starter-us-west-1.openshiftapps.com

## Directory

There are two .db files and two folders storing data of this website. Mydb.db is a file that store all user information. After initializing, admin can login with username: admin and password:admin to login to the system.

photo.db is the file that store the photo data users have submitted, including the owner, mode and the filename of the photos.

The actual photos are stored in /Photos and the CGI scripts are stored in cgi-bin.

## Procedure

The project mainly consists of three main parts, including login procedure, photo database browsing and photo uploading. In homepage.py, user can login to the system, or press add new account to registrate for a new account. Once a user is logged in, he/she will be directed to index.py. In the index page, users can browse photos that are visible to them. When a user choose a file and click upload, users will be directed to upload.py which validate their upload and filter.py to apply filter for the photo. At this point the user can select "discard" or "confirm" to discard or save the photo. After that, the user will be directed back to the Index Page.

## Key Components

The project is built on python3.6 with sqlite3 as the database package and PIL/pillow as the library used for image manipulation

##Review
I have failed to implement cookies but each user are still able to browse their own lists of photos.