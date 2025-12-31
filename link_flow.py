''' heres the flow
    the starting site is the advanced search tool for LSE
    the latest filings are in the first pages 
    
    the flow is to get the links and simultaneously scrape the filings for the links list


'''

from multiprocessing import Process

import link_analyser

import linkscrape_v2

def main():
    
    p1 = Process(target=linkscrape_v2.scrape_links())
    p1.start()
    p2 = Process(target=link_analyser.main())
    p2.start()
    p1.join()
    p2.join()
    

if __name__ == '__main__':
    main()
