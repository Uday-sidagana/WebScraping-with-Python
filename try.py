import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

'''print(soup.title)
print(soup.title.string)
a= soup.find_all('a')[0]
print(a.get("href"))
print(soup.get_text())

print(soup.find_all('div')[0])

s= soup.find(id="Syndrome")
print(s)
print(s.get("href"))'''

'''soup.select(div.x) -- <div class="x">
soup.select(div#x) -- <div id="x">'''

'''ulTag = soup.new_tag("ul")
ltTag = soup.new_tag("lt")
ltTag.name = "SIDAGNANA"

ulTag.append(ltTag)

soup.html.body.insert(0, ulTag)

with open("modify.html", "w") as f:
    f.write(str(soup))
'''