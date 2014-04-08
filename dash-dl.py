#!/usr/bin/env python

from rauth import OAuth1Session
from colors import colorz
from colors_html import gen_html
from urllib import urlretrieve
from os import path
import json


with open('CREDS') as c:
    config = c.read().splitlines()

tumblr = OAuth1Session(
    consumer_key = config[0],
    consumer_secret = config[1],
    access_token = config[2],
    access_token_secret = config[3])
base_url='https://api.tumblr.com/v2'

colors_file = 'html/colors.json'
combos = json.loads(open(colors_file).read())

dash = tumblr.get(base_url + '/user/dashboard', params={'type': 'photo'})
posts = dash.json()['response']['posts']
for latest_post in posts:
    post_slug = latest_post['slug'] or latest_post['reblog_key']
    photo_url = latest_post['photos'][0]['original_size']['url']
    photo_ext = path.splitext(photo_url)[1]
    if photo_ext != ".gif":
        photo_path = path.join("img", post_slug + photo_ext)
        print photo_path
        urlretrieve(photo_url, photo_path)
        try:
            hexes = colorz(photo_path, n=4)
        except TypeError:
            print "This photo ain't go no colors"
        except IndexError:
            print "This photo ain't got enough colors!"
        except IOError:
            print "This photo got corrupted."
        html = gen_html(post_slug, hexes)
        filename = path.join("html", post_slug + ".html")
        with open(filename, 'w') as f:
            f.write(html)
        combos[post_slug] = hexes

with open(colors_file, 'w') as f:
    f.write(json.dumps(combos))
