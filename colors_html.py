#!/usr/bin/env python

from os import path
from bs4 import BeautifulSoup
from colors import colorz

def gen_html(slug, hexes):
    tmpl = BeautifulSoup(open('kmeans.html'))
    tmpl.title.string = slug
    tmpl.select("#one")[0]["style"]   = "background-color:" + hexes[0]
    tmpl.select("#two")[0]["style"]   = "background-color:" + hexes[1]
    tmpl.select("#three")[0]["style"] = "background-color:" + hexes[2]
    tmpl.select("#four")[0]["style"]  = "background-color:" + hexes[3]
    return tmpl.prettify()

if __name__ == "__main__":
    from sys import argv
    try:
        hexes = colorz(argv[1], n=4)
        slug = path.split(path.splitext(argv[1])[0])[1]
        html = gen_html(slug, hexes)
        filename = path.join("html", slug + ".html")
        with open(filename, 'w') as f:
            f.write(html)
    except TypeError:
        print "This photo ain't go no colors"
    except IndexError:
        print "This photo ain't got enough colors!"
    except IOError:
        print "This photo got corrupted."

