import csv

from app.crawler import Crawler
from config import *

def init() -> None:
    crawl = Crawler(ROOT_URL)
    crawl.get()
    crawl.province_get()
    obj = crawl.province_url(LIST_PROVINCE_TH)
    crawl.temple_get(obj)

def temple_dict(province: str):
    lst_temple = []
    with open(f'{ province }.csv') as file:
        reader = csv.reader(file, delimiter = ',', quotechar = '\n')
        lst_temple = [row[0] for row in reader]

    return lst_temple