

from selenium import webdriver
from pyshadow.main import Shadow
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



url = "https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088"


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(5)


tables = driver.find_elements(By.TAG_NAME, 'table')
if not tables:
    '''

    if the normal search for <table> elements doesnt bring anything
    it searches the shadow roots
    
    '''
    shadow = Shadow(driver)
    tables = shadow.find_elements('table')

for table in tables:
    print(table.text)
