import requests
from bs4 import BeautifulSoup
# url for scrapping
url = "https://www.codewithharry.com/"

req = requests.get(url)
# get the html
html = req.content
# parse the html
soup = BeautifulSoup(html, "html.parser")
# get the content from html
title = soup.title
# commonly used types of objects:
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. comment
# print(type(title))

# paras = soup.find_all("p")
# print(paras)

print(soup.find('a').get_text())

anchors = soup.find_all("a")
print(anchors)
for link in anchors:
    if link != "#":
      print(link.get("href"))

# data types in python
# x = "name" string
# x = ["a","b","c"] tuple
# x = range(9)  range
# x = {"name","john","age"} set
# x = {"name":"john", "age" : 22} dict
# x = frozenset({"apple","banana","cherry"})  frozenset
# x= true
# x = b"hello" bytes 
#  x = bytearray(5) bytearray
# x = memoryview(bytes(5)) memoryview 
# x= none Nonetype
