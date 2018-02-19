.PHONY : all clean server
all: README.html

README.html: README.rst
	rst2html README.rst README.html

server:
	python3 http-server.py

