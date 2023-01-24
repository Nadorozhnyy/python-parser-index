import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
from fake_useragent import UserAgent
import cloudscraper

URL_TEMPLATE = "https://ru.investing.com/equities/"
FILE_NAME = "test.csv"


def parser():
    result_list = {'name': [], 'price': []}
    scraper = cloudscraper.create_scraper()
    response = scraper.get(URL_TEMPLATE)
    print(response.status_code)
    soup = bs(response.text, "html.parser")
    index_data = soup.find_all('table', id='cross_rate_markets_stocks_1')

    for el in soup.select('#cross_rate_markets_stocks_1 > tbody > tr'):
        # print(el.a['title'])
        print(el.a['data'])
        # print(el)


parser()


