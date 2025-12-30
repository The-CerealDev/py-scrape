import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


def get_links(driver):

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dash-link')))
    for i in range(4):
                
        try:
                    
            links = driver.find_elements(By.CLASS_NAME,'dash-link')
            links = [link.get_attribute('href') for link in links]
            break
        except:
            continue
    newlist = []
    with open('links_v2.txt', 'a') as file:
        for link in links:
            with open('links_v2.txt', 'r') as rfile:
                    
                if link.strip() in [l.strip() for l in rfile.readlines()]:
                    pass
                else:
                    file.write(f'{link}\n')
                    newlist.append(link)
    return(len(newlist))
    
    # print(links)
    return True

def check_for500(driver):
        if '500' in driver.find_element(By.CSS_SELECTOR,'.results-header').text:
            return True
        else:
            return False
        
def next_page(driver):
    next_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".page-number.active + a")))
    nextpage = next_btn.text
    # next_btn.click()
    if nextpage != 'Last page':
        driver.execute_script("arguments[0].click();", next_btn)
    else:
        print("End of the Page")
        driver.close()
        raise ('Page end reached')


def scrape_links(company= "Blackrock", start = '20250101', end = '20260101'):
        
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = f'https://www.londonstockexchange.com/news?tab=news-explorer&headlinetypes=&excludeheadlines=&headlines=162&period=custom&beforedate={start}&afterdate={end}&namecode={company}&page=1'

    driver.get(url)

    try:

        cookiebtn = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,'#onetrust-reject-all-handler'))
    )
        cookiebtn.click()
    except:
        sys.stdout.write('NoCOokie')


    fieldselector = '.ng-input'
    
    time.sleep(2)
    nextpageselector = '.page-number.active + .page-number'

    fselect = driver.find_element(By.CSS_SELECTOR,fieldselector)

    fselect.click()

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ng-dropdown-panel"))
    )


    option_500 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='ng-option-label' and contains(text(), 'Show 500 news')]"))
    )
    option_500.click()

    




    WebDriverWait(driver, 10).until(
        check_for500
    )
    stuff = False
    page_no  = 1
    while not stuff:
        current_page = int(driver.find_element(By.CSS_SELECTOR, '.page-number.active').text)
        print(current_page)

        links = get_links(driver)
        page_no +=1
        print(f'Got {links} new links, Next Page({page_no})...')
        if links == 0:
            print(f"No new links, Quitting process...")
            break
        next_page(driver)
    driver.close()

def main():
    scrape_links()

if __name__ == "__main__":
    main()