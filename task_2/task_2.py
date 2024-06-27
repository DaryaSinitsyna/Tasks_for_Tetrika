import logging

import requests
from bs4 import BeautifulSoup as Soup
import csv

PREFIX_URL = 'https://ru.wikipedia.org'
SITE_URL = f'{PREFIX_URL}/wiki/Категория:Животные_по_алфавиту'
FILE_NAME = 'beasts.csv'


def parse_page(response, result):
    soup = Soup(response.content, 'lxml')
    block = soup.find('div', id='mw-pages')
    if not block:
        return None, result

    categories = block.find_all('div', class_='mw-category-group')
    site_url = None

    if not categories:
        return None, result

    for category in categories:
        symbol = category.find('h3').text

        if not symbol.isalpha():
            continue
        if not 1040 <= ord(symbol) <= 1072:
            break
        count_elem = result.get(symbol, 0)
        result[symbol] = count_elem + len(category.find_all('li'))

        if not block.find('a', string='Следующая страница'):
            break
        site_url = PREFIX_URL + block.find('a', string='Следующая страница').get('href')

    return site_url, result


def save_to_file(result, filename):
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in result.items():
                writer.writerow([key, value])
    except Exception as ex:
        logging.exception(ex)
        return


def fetch_wikipedia_page(site_url):
    response = requests.get(site_url)
    response.raise_for_status()
    return response


def parse_wikipedia_animals(url):
    site_url = url
    result = {}
    filename = FILE_NAME

    while site_url:
        try:
            response = fetch_wikipedia_page(site_url)
            site_url, result = parse_page(response, result)
        except Exception as ex:
            logging.exception(ex)
            return

    save_to_file(result, filename)


if __name__ == "__main__":
    parse_wikipedia_animals(SITE_URL)
