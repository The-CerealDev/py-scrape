#This is where the configuration variables will be stored
import os

# Project root directory (parent of config/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COMPANY = "Blackrock"
START_DATE = '20250101'
END_DATE = '20260101'

LINK_LIST = os.path.join(BASE_DIR, 'results', f'{COMPANY}-links.txt')
SCRAPE_CSV = os.path.join(BASE_DIR, 'results', f'{COMPANY}-scraped.csv')
SKIPPED_LINKS = os.path.join(BASE_DIR, 'results', f'{COMPANY}-skipped.txt')
CLEAN_LINKS = os.path.join(BASE_DIR, 'results', f'{COMPANY}-links-cleaned.txt')