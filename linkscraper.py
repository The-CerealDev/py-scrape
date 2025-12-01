from selenium import webdriver
from pyshadow.main import Shadow
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

'''
This would be scraping the London Stock Exchange site for the form 8.3 links 
'''
page_file = 'lastpage.txt'
with open(page_file,'r') as file:
    # file.writelines("1")
    last_page = int(file.readline())
    print(last_page)


links = []
def scrape_links(starting_page):
    global links
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    print(f"Going to page {starting_page}")
    news_sect = f"https://www.londonstockexchange.com/search?searchtype=news&page={starting_page}&q=blackrock%208.3"
    
    driver.get(news_sect)
    time.sleep(3)
    urls = driver.find_elements(By.CLASS_NAME,'news-link')
    for url in urls:
        links.append(url.text)
    print(links)

   

def main():
    global last_page
    for i in range(100):
                
        scrape_links(last_page)
        
        last_page +=1
        with open(page_file, 'w') as file:
            file.write(str(last_page))

        with open("result_links.txt", "a") as file:
            file.writelines([line + '\n' for line in links])

    

if __name__ == "__main__":
    main()
