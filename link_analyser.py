import pandas as pd

import pyscrape

chrome_options = pyscrape.Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
service = pyscrape.Service(pyscrape.ChromeDriverManager().install())
driver = pyscrape.webdriver.Chrome(options=chrome_options, service=service)

urls = []
current_var = pd.read_csv("scrape-blackrock.csv")
scraped = set(current_var["Link"])
with open("links_cleaned.txt", "r") as file:
    for line in file.readlines():
        if line in scraped:
            continue
        try:
            obj = pyscrape.scrape(line, driver)
            var = pd.DataFrame([obj])
            var.to_csv("scrape-blackrock.csv", mode="a", index=False, header=False)

        except Exception as e:
            print(f"Error scraping {line}: {e}")


# obj = pyscrape.scrape(
#     "https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088"
# )

# obj = {
#     "Company": "Just Group plc",
#     "Index": "",
#     "Filing": "Form 8.3",
#     "Position Date": "24 November 2025",
#     "Voting Rights": 59335996,
#     "%(voting)": 5.71,
#     "Other Instruments": 39339386,
#     "%(other)": "3.78",
#     "Total voting rights": "98675382",
#     "Shares with no voting rights": 2934681,
#     "%(of shares)": 4.95,
#     "%(ISC)": 0.2824,
#     "Link": "https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088",
# }
# # print(obj)
# var = pd.DataFrame([obj])
# print(var)

# var.to_csv("scrape-blackrock.csv")
# print(var["Company"])
# var.loc[len(var)] = obj
# print(var)
# var.to_csv("scrape-blackrock.csv")
