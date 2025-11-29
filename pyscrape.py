

from selenium import webdriver
from pyshadow.main import Shadow
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def validateURL(url):
    raise NotImplementedError("I Cereal_Dev have not implemented ths feature yet...")

url = input("Enter the URL to scrape: ")
if not url:
    url = "https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088"
else:
    validateURL(url)

print(f"Getting URL:{url}...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(3)


tables = driver.find_elements(By.TAG_NAME, 'table')

test = {

}  
if not tables:
    '''

    if the normal search for <table> elements doesnt bring anything
    it searches the shadow roots
    
    '''
    shadow = Shadow(driver)
    tables = shadow.find_elements('table')
    if not tables:
        print("NOT FOUND, \nthis could be because of the browser or i just havent implemented this right?")

for i,table in enumerate(tables[0:2], 1):
    print(f"============Table {i}============")
    rows = table.find_elements(By.TAG_NAME,'tr')
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >=2:
            field = cells[0].text
            value = [element.text for element in cells[0:]]
            test[field] = value
    print(test)
    test ={


    }
        # print(row.text)
    




    
data = {
    "Company":"",
    "Index": "",
    "Filing": "",
    "Position Date": "",
    "Voting Rights": 0,
    "%(voting)": 0,
    "Other Instruments": 0,
    "%(other)": 0,
    "Total voting rights": 0,
    "Shares with no voting rights": 0,
    "%(shares)": 0,
    "%(ISC)": 0,
    "link": ""
}


