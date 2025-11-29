##Starting test code to just scrape the <table> elements in any page and parse it 
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# web = requests.get('https://github.com/the-cerealdev')
# web = requests.get('https://www.londonstockexchange.com/news-article/market-news/form-8-3-just-group-plc/17344088') #this happens to be a dynamic website
url='https://www.w3schools.com/html/html_tables.asp'
web = requests.get('https://www.w3schools.com/html/html_tables.asp')
soup = BeautifulSoup(web.content,'html.parser')

tables = soup.find('table')
print(tables)
if tables:
    print(tables)
else:
    print('no tables found')
print(web.status_code)

with open('output.html', 'w', encoding='utf-8') as f:
    f.write('<html><head><meta charset="utf-8"></head><body>')
    f.write('<style>')
    for style_tag in soup.find_all('style'):
        f.write(style_tag.get_text())
    for link in soup.find_all('link', rel='stylesheet'):
        css_link = urljoin(url,link['href'])
       
        css_response = requests.get(css_link)
        f.write(str(css_response))
    f.write('</style>')
    for element in tables:
        
        f.write(str(element))

    f.write('</body></html>')


f.close()
# print(soup.prettify())