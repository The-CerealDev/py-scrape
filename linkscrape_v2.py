import time

from pyshadow.main import Shadow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


def get_links(driver):
    links = driver.find_elements(By.CLASS_NAME,'dash-link')
    links = [link.text for link in links]
    print(links)
    return()

with open('clicks.txt','r') as file:
    clicks = int(file.readlines()[0])
    print(clicks)

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.londonstockexchange.com/news?tab=news-explorer&headlinetypes=&excludeheadlines=&headlines=162&period=custom&beforedate=20251220&afterdate=20250101&namecode=Blackrock&page=1'

driver.get(url)

try:

    cookiebtn = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.CSS_SELECTOR,'#onetrust-reject-all-handler'))
)
    cookiebtn.click()
except:
    sys.stdout.write('NoCOokie')


fieldselector = '.ng-input'
selector500 = '#aa9fdb011d19-3'

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

time.sleep(2)
get_links(driver)
