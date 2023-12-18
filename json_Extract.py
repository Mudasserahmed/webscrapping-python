import requests
from bs4 import BeautifulSoup
import json

# url for scrapping
url = "https://www.codewithharry.com/"

req = requests.get(url)

if req.status_code == 200:
    # get the html
    html = req.content
    # parse the html
    soup = BeautifulSoup(html, "html.parser")

    # get the content from html
    title = soup.title

    # Extract data for JSON
    data_dict = {"title": title.get_text(), "links": []}
    anchors = soup.find_all("a")

    for link in anchors:
        if link.get("href") != "#":
            data_dict["links"].append({"text": link.get_text(), "url": link.get("href")})

    # Save JSON data to a file
    with open("scraped_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, indent=2)

    print("Data has been successfully extracted to 'scraped_data.json'.")
else:
    print(f"Failed to retrieve the page. Status code: {req.status_code}")
