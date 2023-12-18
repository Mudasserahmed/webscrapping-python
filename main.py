import requests
from bs4 import BeautifulSoup
import csv
import shutil

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

 # Create a CSV file and write headers
    with open("scraped_title.csv", "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["title", "title text"])
   
       #GET TITLE
        title_text = title.get_text()
        csv_writer.writerow([title, title_text])
      
        # Loop through each anchor tag and extract data
        for link in anchors:
            link_text = link.get_text()
            link_url = link.get("href")

              
         
            # Skip links with href="#"
            if link_url != "#":
                csv_writer.writerow([link_text, link_url])

    print("Data has been successfully extracted to 'scraped_data.csv'.")

    # # Move the CSV file to a desired location (replace "path/to/destination" with your desired path)
    # destination_path = "path/to/destination/scraped_data.csv"
    # shutil.move("scraped_data.csv", destination_path)
    
    # print(f"CSV file has been downloaded to: {destination_path}")
else:
    print(f"Failed to retrieve the page. Status code: {req.status_code}")