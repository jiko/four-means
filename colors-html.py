from os import path
from bs4 import BeautifulSoup
from sys import argv
from colors import colorz

photo_path = argv[1]

try:
    hexes = colorz(photo_path, n=4)
except TypeError:
    print "This photo ain't go no colors"
except IndexError:
    print "This photo ain't got enough colors!"
except IOError:
    print "This photo got corrupted."

post_slug = photo_path[4:-4]
filename = path.join("html", post_slug + ".html")
tmpl = BeautifulSoup(open('kmeans.html'))
with open(filename, 'w') as f:
    tmpl.title.string = post_slug
    tmpl.select("#one")[0]["style"]   = "background-color:" + hexes[0]
    tmpl.select("#two")[0]["style"]   = "background-color:" + hexes[1]
    tmpl.select("#three")[0]["style"] = "background-color:" + hexes[2]
    tmpl.select("#four")[0]["style"]  = "background-color:" + hexes[3]
    f.write(tmpl.prettify())
