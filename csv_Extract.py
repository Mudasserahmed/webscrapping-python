import requests
from bs4 import BeautifulSoup
import csv

# url for scrapping
url = "https://github.com/"

req = requests.get(url)

if req.status_code == 200:
    # get the html
    html = req.content
    # parse the html
    soup = BeautifulSoup(html, "html.parser")

    # get the content from html
    title = soup.title
    anchors = soup.find_all("a")

    # Extract data for CSV
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["title", "link_text", "link_url"])

        title_text = title.get_text()
        for link in anchors:
            link_text = link.get_text()
            link_url = link.get("href")

            # Skip links with href="#"
            if link_url != "#":
                csv_writer.writerow([title_text, link_text, link_url])

    print("Data has been successfully extracted to")
