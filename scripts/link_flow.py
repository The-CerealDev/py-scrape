''' heres the flow
    the starting site is the advanced search tool for LSE
    the latest filings are in the first pages 
    
    the flow is to get the links and simultaneously scrape the filings for the links list


'''
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from multiprocessing import Process

import link_analyser

import linkscrape_v2

from config import COMPANY, START_DATE, END_DATE

def main():
    
    #Fixed the multiprocessing concurrency issue by using the Process class instead of the Pool class
    p1 = Process(target=linkscrape_v2.scrape_links, kwargs={'company': COMPANY, 'start': START_DATE, 'end': END_DATE})
    p1.start()
    p2 = Process(target=link_analyser.main)
    p2.start()
    p1.join()
    p2.join()
    

if __name__ == '__main__':
    main()
