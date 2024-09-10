import datetime

import requests

from bs4 import BeautifulSoup

url ="https://thehoppygoatfarm.com/2018/03/egg-yolk-coffee-yup-thing-awesome/"

def FetchAndSave(url, path):
    r = requests.get(url)

    with open(path, "w") as f:
        f.write(r.text)

FetchAndSave(url, "WebScraping/Data/text.html")
