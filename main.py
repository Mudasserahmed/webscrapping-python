import requests
from bs4 import BeautifulSoup
# url for scrapping
url = "https://www.freecodecamp.org/"

req = requests.get(url)
# get the html
html = req.content
# parse the html
soup = BeautifulSoup(html,"html.parser")
# get the content from html
title = soup.title
# commonly used types of objects:
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. comment
print(type(title))
