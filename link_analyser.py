import pandas as pd

import pyscrape
import csv
chrome_options = pyscrape.Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
service = pyscrape.Service(pyscrape.ChromeDriverManager().install())
driver = pyscrape.webdriver.Chrome(options=chrome_options, service=service)

urls = []
current_var = pd.read_csv("Blackrock-non-dupe.csv")
scraped = set(current_var["Link"].str.strip())
# print(scraped)
with open("links_cleaned.txt", "r") as file:
    for line in file.readlines():
        if line.strip() in scraped:
            print('DUPE')
            continue
        # try:
        obj = pyscrape.scrape(line, driver)
        var = pd.DataFrame([obj])
        var.to_csv("Blackrock-non-dupe.csv", mode="a", quoting=csv.QUOTE_MINIMAL, index=False, header=False, escapechar='\\', lineterminator='\n')

        # except Exception as e:
        #     print(f"Error scraping {line}: {e}")

