import pyscrape
import pandas as pd
urls = []
# with open('links_cleaned.txt','r') as file:
#     for line in file.readlines():
#         pyscrape.scrape(line)
        

obj = pyscrape.scrape("https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088")


print(obj)
var = pd.DataFrame([obj])
print(var)