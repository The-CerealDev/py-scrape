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
    # validateURL(url)
    pass

print(f"Getting URL:{url}...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(3)


tables = driver.find_elements(By.TAG_NAME, 'table')
main = {

}
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
            if not field:
                field = "--"
            value = [element.text for element in cells[1:]]
            test[field] = value
    print(test)
    main.update(test.copy())
    test ={


    }
        # print(row.text)
    

main['TOTAL'] = main['       TOTAL:']
del main["       TOTAL:"]
total = main["TOTAL"][0].replace(',',"")
main['TOTAL'][0] = total
main['(1) Relevant securities owned and/or controlled:'][0] = main['(1) Relevant securities owned and/or controlled:'][0].replace(',','')
    
data = {
    "Company":main["(c) Name of offeror/offeree in relation to whose relevant securities this form relates:\n     Use a separate form for each offeror/offeree"][0],
    "Index": "",
    "Filing": "Form 8.3",
    "Position Date": main['(e) Date position held/dealing undertaken:\n     For an opening position disclosure, state the latest practicable date prior to the disclosure'][0],
    "Voting Rights": int(main['(1) Relevant securities owned and/or controlled:'][0]),
    "%(voting)": float(main['(1) Relevant securities owned and/or controlled:'][1][:-1]),
    "Other Instruments": int(main['TOTAL'][0])-int(main['(1) Relevant securities owned and/or controlled:'][0]),
    "%(other)": float(main['TOTAL'][1][:-1])-float(main['(1) Relevant securities owned and/or controlled:'][1][:-1]),
    "Total voting rights": main['TOTAL'][0],
    "Shares with no voting rights": 0,
    "%(shares)": 0,
    "%(ISC)": 0,
    "link": ""
}


print(f"Company : {data['Company']}\nPosition Date : {data["Position Date"]} \nVoting Rights : {data["Voting Rights"]:,}\n%Voting : {data['%(voting)']}\nOther Instruments : {data['Other Instruments']:,}")