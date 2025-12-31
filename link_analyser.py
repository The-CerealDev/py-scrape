import pandas as pd

import pyscrape
import csv
import sys
def main():
        
    chrome_options = pyscrape.Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    service = pyscrape.Service(pyscrape.ChromeDriverManager().install())
    driver = pyscrape.webdriver.Chrome(options=chrome_options, service=service)

    skipped = []
    max_tries = 3
    scrape_csv = 'Blackrock-non-dupe.csv'
    link_list = 'linksv2 _cleaned.txt'
    skipped_links = 'skipped_links.txt'


    urls = []
    current_var = pd.read_csv(scrape_csv)
    scraped = set(current_var["Link"].str.strip())
    # print(scraped)
    with open(link_list, "r") as file:
        for line in file.readlines():
            if line.strip() in scraped:
                sys.stdout.write('DUPE')
                continue
            tries = 0
            while tries <= max_tries:
                
                try:
                        
                    obj = pyscrape.scrape(line, driver)
                    sys.stdout.write(f'Scraped {line} successfully\n')
                    var = pd.DataFrame([obj])
                    var.to_csv(scrape_csv, mode="a", quoting=csv.QUOTE_MINIMAL, index=False, header=False, escapechar='\\', lineterminator='\n')
                    break
                except Exception as e:
                    sys.stdout.write(f"Error scraping {line}: {e}")
                    tries += 1
                    if tries == max_tries:
                        sys.stdout.write(f'SKIPPING {line}...')
                        with open(skipped_links, 'a') as afile:
                            afile.writelines([line,str(e)])
                        break

if __name__ == '__main__':
    main()