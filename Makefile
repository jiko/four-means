.PHONY: clean all more

all: more html/list.html

more:
	dash-dl.py

html/list.html: html/*.html
	ls html/*.html | sed 's/html\///' | grep -v index.html | grep -v list.html | list-html.sh > $@

clean:
	rm *.pyc img/*
