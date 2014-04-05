from os import path, listdir
from bs4 import BeautifulSoup
import json

pages = listdir("./html")
pages.remove('index.html')
pages.remove('list.html')
combos = []

for page in pages:
    if page[-4:] == 'html':
      colors = dict()
      html = BeautifulSoup(open('./html/'+page))
      hexes = [html.select(div)[0]["style"].replace("background-color:","") for div in ["#one","#two","#three","#four"]]
      colors[html.title.string.strip()] = hexes
      combos.append(colors)

filename = path.join("html", "colors.json")
with open(filename, 'w') as f:
    f.write(json.dumps(combos))
