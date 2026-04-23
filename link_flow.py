''' heres the flow
    the starting site is the advanced search tool for LSE
    the latest filings are in the first pages 
    
    the flow is to get the links and simultaneously scrape the filings for the links list


'''

from multiprocessing import Process

import link_analyser

import linkscrape_v2

from config import COMPANY, START_DATE, END_DATE

#An error in the multiprocessing concurrency of the two function needs to be fixed
def main():
    
    #company = "Schroders"
    p1 = Process(target=linkscrape_v2.scrape_links(company=COMPANY, start=START_DATE, end=END_DATE))
    p1.start()
    p2 = Process(target=link_analyser.main())
    p2.start()
    p1.join()
    p2.join()
    

if __name__ == '__main__':
    main()
