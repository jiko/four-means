from rauth import OAuth1Session
from bs4 import BeautifulSoup
from colors import colorz
from urllib import urlretrieve
from os import path


with open('CREDS') as c:
    config = c.read().splitlines()

tumblr = OAuth1Session(
    consumer_key = config[0],
    consumer_secret = config[1],
    access_token = config[2],
    access_token_secret = config[3])
base_url='https://api.tumblr.com/v2'
dash = tumblr.get(base_url + '/user/dashboard', params={'type': 'photo'})
posts = dash.json()['response']['posts']

for latest_post in posts:
    post_slug = latest_post['slug'] or latest_post['reblog_key']
    photo_url = latest_post['photos'][0]['original_size']['url']
    photo_ext = photo_url[-4:]
    if photo_ext != ".gif":
        photo_path = path.join("img", post_slug + photo_ext)
        print photo_path
        urlretrieve(photo_url, photo_path)
        try:
            hexes = colorz(photo_path, n=4)
            tmpl = BeautifulSoup(open('kmeans.html'))
            filename = path.join("html", post_slug + ".html")
            with open(filename, 'w') as f:
                tmpl.title.string = post_slug
                tmpl.select("#one")[0]["style"]   = "background-color:" + hexes[0]
                tmpl.select("#two")[0]["style"]   = "background-color:" + hexes[1]
                tmpl.select("#three")[0]["style"] = "background-color:" + hexes[2]
                tmpl.select("#four")[0]["style"]  = "background-color:" + hexes[3]
                f.write(tmpl.prettify())
        except TypeError:
            print "This photo ain't go no colors"
        except IndexError:
            print "This photo ain't got enough colors!"
        except IOError:
            print "This photo got corrupted."
