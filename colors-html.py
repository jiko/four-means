#!/usr/bin/env python

from os import path
from bs4 import BeautifulSoup
from colors import colorz

def gen_html(photo_path):
    hexes = colorz(photo_path, n=4)
    slug = path.split(path.splitext(photo_path)[0])[1]
    filename = slug + ".html"
    tmpl = BeautifulSoup(open('kmeans.html'))
    with open(filename, 'w') as f:
        tmpl.title.string = slug
        tmpl.select("#one")[0]["style"]   = "background-color:" + hexes[0]
        tmpl.select("#two")[0]["style"]   = "background-color:" + hexes[1]
        tmpl.select("#three")[0]["style"] = "background-color:" + hexes[2]
        tmpl.select("#four")[0]["style"]  = "background-color:" + hexes[3]
        f.write(tmpl.prettify())

if __name__ == "__main__":
    from sys import argv
    try:
        gen_html(argv[1])
    except TypeError:
        print "This photo ain't go no colors"
    except IndexError:
        print "This photo ain't got enough colors!"
    except IOError:
        print "This photo got corrupted."

