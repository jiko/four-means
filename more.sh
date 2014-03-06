#!/bin/zsh

# Should this be a Makefile?

python dash.py
cd html
ls *.html | grep -v index.html | ../index-html.sh > index.html
