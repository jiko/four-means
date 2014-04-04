#!/bin/zsh

# Should this be a Makefile?

python dash.py
cd html
ls *.html | grep -v index.html | grep -v list.html | grep -v pages.json | ../list-html.sh > list.html
cd ../
pages-json.py > html/pages.json
