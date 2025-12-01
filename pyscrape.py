from selenium import webdriver
from pyshadow.main import Shadow
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv 

def validateURL(url):
    raise NotImplementedError("I Cereal_Dev have not implemented ths feature yet...")

def scrape(url):
    global main
    global data
    test = {
         

    } 
    print(f"Getting URL:{url}...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    time.sleep(3)


    # tables = driver.find_elements(By.TAG_NAME, 'table')
    tables = driver.find_elements(By.CLASS_NAME,'do')
      
    if not tables:
        '''

        if the normal search for <table> elements doesnt bring anything
        it searches the shadow roots
        
        '''
        shadow = Shadow(driver)
        # tables = shadow.find_elements('table')
        tables = shadow.find_elements('.do')
        non_voting_fine_print = shadow.find_elements('.do + p .dj')
        fine_list = non_voting_fine_print[1].text.split()
        non_voting = fine_list[-7] #negative index to find the non voting rights in the fine print 


        if not tables:
            print("NOT FOUND, \nthis could be because of the browser or i just havent implemented this right?")

    for i,table in enumerate(tables[0:2], 1):
        # print(f"============Table {i}============")
        rows = table.find_elements(By.TAG_NAME,'tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >=2:
                field = cells[0].text
                if not field:
                    field = "--"
                value = [element.text for element in cells[1:]]
                test[field] = value
        # print(test)
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
        "%(other)": f"{float(main['TOTAL'][1][:-1])-float(main['(1) Relevant securities owned and/or controlled:'][1][:-1]):.2f}",
        "Total voting rights": main['TOTAL'][0],
        "Shares with no voting rights": int(non_voting.replace(',','')),
        "%(of shares)": float(f"{((int(non_voting.replace(',','')) / int(main['(1) Relevant securities owned and/or controlled:'][0])) * 100):.2f}"),
        "%(ISC)": float(f"{((int(non_voting.replace(',','')) / int(main['(1) Relevant securities owned and/or controlled:'][0])) * float(main['(1) Relevant securities owned and/or controlled:'][1][:-1])):.4f}"),
        "Link": url
    }
    class Company:
        def __init__ (self, name, filing, position_date, voting_rights, percent_voting, other_instruments, percent_other, total_voting_rights, shares_no_voting_rights, percent_of_shares, percent_ISC, link):
            self.name = name
            self.filing = filing
            self.position_date = position_date
            self.voting_rights = voting_rights
            self.percent_voting = percent_voting
            self.other_instruments = other_instruments
            self.percent_other = percent_other
            self.total_voting_rights = total_voting_rights
            self.shares_no_voting_rights = shares_no_voting_rights
            self.percent_of_shares = percent_of_shares
            self.percent_ISC = percent_ISC
            self.link = link
    company_instance = Company(
        name = data["Company"],
        filing = data["Filing"],
        position_date = data["Position Date"],
        voting_rights = data["Voting Rights"],
        percent_voting = data["%(voting)"],
        other_instruments = data["Other Instruments"],
        percent_other = data["%(other)"],
        total_voting_rights = data["Total voting rights"],
        shares_no_voting_rights = data["Shares with no voting rights"],
        percent_of_shares = data["%(of shares)"],
        percent_ISC = data["%(ISC)"],
        link = data["Link"]
    )
    for attr, value in company_instance.__dict__.items():
        print(f"{attr}: {value}")




url = input("Enter the URL to scrape: ")
if not url:
    url = "https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088"
else:
    validateURL(url)
    # pass
main={

}
data = {

}
scrape(url)


big_data= [

]
big_data.append(data)

# filename = 'scrape-data.csv'

# with open(filename, mode ='w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=data.keys())
#     writer.writeheader()
#     writer.writerow(data)

# print(f"Company : {data['Company']}\nPosition Date : {data["Position Date"]} \nVoting Rights : {data["Voting Rights"]:,}\n%Voting : {data['%(voting)']}\nOther Instruments : {data['Other Instruments']:,}")
# print(f"Non Voting rights: {data['Shares with no voting rights']:,}")
# print(f"%Non Voting: {data['%(shares)']}")
# print(f"%ISC: {data['%(ISC)']}")