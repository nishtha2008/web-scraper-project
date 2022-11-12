import csv
from bs4 import BeautifulSoup
import requests

WEBSITE_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#avoiding SSL error
webpage = requests.get(WEBSITE_URL, verify = False)

headers = ["V Mag. (mV)", "Proper name", "Bayer designation", "Distance (ly)", "Spectral class", "Mass (M☉)", "Radius (R☉)", "Luminosity (L☉)"]

#webpage.text returns in html format
soup = BeautifulSoup(webpage.text, "html.parser")

#97 rows excluding header
table = soup.find('table')

#0 row contains headers
table_rows = table.find_all(['tr'])[1:]

with open("scraper.csv", "w", encoding = "utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(headers)

    for rows in table_rows:

        #each entry is in td
        table_data = rows.find_all('td')

        #removing newlines by replacing them with blank
        row = [data.text.replace('\n','') for data in table_data]

        writer.writerow(row)