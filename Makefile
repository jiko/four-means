.PHONY: clean

clean:
	rm *.pyc img/*

html/list.html: html/*.html
	ls html/*.html | sed 's/html\///' | grep -v index.html | grep -v list.html | list-html.sh > html/list.html
