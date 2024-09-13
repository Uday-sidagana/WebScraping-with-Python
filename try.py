import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()
# Beautiful soup object
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

'''cont= soup.find(class_="container")
print(cont.has_attr("class"))

def has_class_not_id(tag):
 return tag.has_attr("class") and not tag.has_attr("id")

results= soup.find_all(has_class_not_id)
print(results)'''


'''def no_class_no_id(tag):
   return not tag.has_attr("class") and not tag.has_attr("id")

results2 = soup.find_all(no_class_no_id)
print(results2)'''

'''
def has_lang(tag):
    return tag.has_attr("lang")

results3 = soup.find_all(has_lang)
print(results3)'''