import datetime

import requests

from bs4 import BeautifulSoup

url ="https://en.wikipedia.org/wiki/Grenade"

def FetchAndSave(url, path):
    r = requests.get(url)

    with open(path, "w") as f:
        f.write(r.text)

FetchAndSave(url, "Data/text.html")
