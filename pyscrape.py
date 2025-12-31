import time

from pyshadow.main import Shadow
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def validateURL(url):
    raise NotImplementedError("I Cereal_Dev have not implemented ths feature yet...")


def scrape(
    url="https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088",
    driver="pluh",
):
    global maindict
    global data

    test = {}
    sys.stdout.write("\033[F")  # Cursor up one line
    print(f"Getting URL:{url}...\n")
    

    driver.execute_script("window.open('')")
    driver.switch_to.window(driver.window_handles[-1])

    driver.get(url)
    shadow = Shadow(driver)
    time.sleep(2)

    # tables = driver.find_elements(By.TAG_NAME, 'table')


    '''
        the tables form obvservation have classes like em do dj etc
        an approach to solve this is to search using all the listed class names above
        however a better approach is to search for all the <table> elements inside the content div 'news-body-content'
    '''
    tables = driver.find_elements(By.CSS_SELECTOR, "table")
    for ell in tables:
        print(ell.text)

    if (not tables):
        """

        if the normal search for <table> elements doesnt bring anything
        it searches the shadow roots

        """
        
        tables = shadow.find_elements("table")
        # non_voting_fine_print = shadow.find_elements(".em + p .el")
        # print(non_voting_fine_print)
        # fine_list = non_voting_fine_print[1].text.split()
        # non_voting = fine_list[
        #     -7
        # ]  # negative index to find the non voting rights in the fine print

        if not tables:
            print(
                "NOT FOUND, \nthis could be because of the browser or i just havent implemented this right?"
            )
    else:
        # non_voting_fine_print = driver.find_elements(By.CSS_SELECTOR,'.do + p .dj')
        # fine_list = non_voting_fine_print[1].text.split()
        # non_voting = fine_list[-7]
        pass

    for i, table in enumerate(tables[0:2], 1):
        # print(f"============Table {i}============")
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 2:
                field = cells[0].text
                if not field:
                    field = "--"
                value = [element.text for element in cells[1:]]
                test[field] = value
        # print(test)
        maindict.update(test.copy())

    non_voting_fine_print = shadow.find_elements("table + p")
    # print(non_voting_fine_print)
    fine_list = non_voting_fine_print[1].text.split() if 'blackrock' in non_voting_fine_print[1].text.lower() else []
    if not fine_list:
        print("Could not find non voting fine print...")
        non_voting = '0,0'                                                        
    else:

        non_voting = fine_list[
            -7
        ]  # negative index to find the non voting rights in the fine print

    """
    The website does not need to be open after this
    """
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # print(maindict)
    test = {}
    # print(row.text)

    # maindict["TOTAL"] = maindict["       TOTAL:"]
    # del maindict["       TOTAL:"]

    try:
        
        discloser = maindict['(a)   Full name of discloser']
    except:
        discloser = maindict['(a) Full name of discloser:']
    if 'blackrock' not in discloser[0].lower() :
        print(f'discloser is not Black rock, {discloser[0]}')
        return'SKIP'

    # for content in maindict:
    #     if 'blackrock' not in content.lower():
    #         print(f'Not Blackrock')
    #         return'skip'

    # total = maindict["Total"][0].replace(",", "")
    try:
        
        maindict['(1)   Relevant securities owned and/or controlled'][0] = maindict[
            '(1)   Relevant securities owned and/or controlled'
        ][0].replace(",", "")

        securities = maindict['(1)   Relevant securities owned and/or controlled']
    except:
        maindict["(1) Relevant securities owned and/or controlled:"][0] = maindict[
            "(1) Relevant securities owned and/or controlled:"
        ][0].replace(",", "")

        securities = maindict['(1) Relevant securities owned and/or controlled:']
    if securities[0].strip() =='0':
        print('Zero Security')
        print(securities)
        percent = 0 
    else:
        percent = (int(non_voting.replace(',', '')) / int(securities[0])) 
    
        
    try:
        total = maindict["Total"]
    except:
        total = maindict["       TOTAL:"]
    try:
            
        offeror_name = maindict[
                "(c) Name of offeror/offeree in relation to whose relevant securities this form relates:\n     Use a separate form for each offeror/offeree"
            ][0].replace('''"''', "")
    except:
        
        offeror_name = maindict['(c)   Name of offeror/offeree in relation to whose relevant securities this form relates\nUse a separate form for each offeror/offeree'][0].replace('''"''', "")

    try:
                
        date = maindict[
                "(e) Date position held/dealing undertaken:\n     For an opening position disclosure, state the latest practicable date prior to the disclosure"
            ][0]
    except:

        date = maindict[
            '(e)   Date position held/dealing undertaken\nFor an opening position disclosure, state the latest practicable date prior to the disclosure'  ][0]



    data = {
        "Company": offeror_name,
        "Index": "",
        "Filing": "Form 8.3",
        "Position Date": date,
        "Voting Rights": int(
            securities[0]
        ),
        "%(voting)": float(
            securities[1][:-1]
        ),
        "Other Instruments": int(total[0].replace(",", ""))
        - int(securities[0]),
        "%(other)": f"{float(total[1][:-1]) - float(securities[1][:-1]):.2f}",
        "Total voting rights": total[0],
        "Shares with no voting rights": int(non_voting.replace(",", "")),
        "%(of shares)": float(
            f"{(percent * 100):.2f}"
        ),
        "%(ISC)": float(
            f"{(percent * float(securities[1][:-1])):.4f}"
        ),
        "Link": url.strip(),
    }

    class Company:
        def __init__(
            self,
            name,
            filing,
            position_date,
            voting_rights,
            percent_voting,
            other_instruments,
            percent_other,
            total_voting_rights,
            shares_no_voting_rights,
            percent_of_shares,
            percent_ISC,
            link,
        ):
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
        name=data["Company"],
        filing=data["Filing"],
        position_date=data["Position Date"],
        voting_rights=data["Voting Rights"],
        percent_voting=data["%(voting)"],
        other_instruments=data["Other Instruments"],
        percent_other=data["%(other)"],
        total_voting_rights=data["Total voting rights"],
        shares_no_voting_rights=data["Shares with no voting rights"],
        percent_of_shares=data["%(of shares)"],
        percent_ISC=data["%(ISC)"],
        link=data["Link"],
    )

    # for attr, value in company_instance.__dict__.items():
    #     print(f"{attr}: {value}")
    sys.stdout.write(f'Scraped {url} successfully\n')
    return data


maindict = {}
data = {}


def main():
    global data
    global maindict

    url = input("Enter the URL to scrape: ")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)

    if not url:
        url = "https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088"
    else:
        # validateURL(url)

        pass

    data = {}
    scrape(url, driver)

    big_data = []

    big_data.append(data)
    print(big_data)

    # filename = 'scrape-data.csv'

    # with open(filename, mode ='w', newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=data.keys())
    #     writer.writeheader()
    #     writer.writerow(data)

    # print(f"Company : {data['Company']}\nPosition Date : {data["Position Date"]} \nVoting Rights : {data["Voting Rights"]:,}\n%Voting : {data['%(voting)']}\nOther Instruments : {data['Other Instruments']:,}")
    # print(f"Non Voting rights: {data['Shares with no voting rights']:,}")
    # print(f"%Non Voting: {data['%(shares)']}")
    # print(f"%ISC: {data['%(ISC)']}")


if __name__ == "__main__":
    main()
