from bs4 import Tag
from src.scrapers.exceptions import USOSError


def check_for_usos_errors(soup):
    title = soup.find('title').text.strip()
    if title == 'USOSweb tymczasowo niedostępny - USOSWEB PW':
        raise RuntimeError('USOS jest aktualnie niedostępny (przerwa techniczna)')
    if title == '503 - Strona tymczasowo niedostępna - USOSWEB PW':
        raise USOSError('Strona jest aktualnie niedostępna (bład 503)')


def deconstruct_table(table: Tag):
    values = {}
    tbody = table.find('tbody')
    for row in tbody.find_all('tr'):
        cells = row.find_all('td')
        key = cells[0].text.strip()
        value = cells[1]
        values[key] = value
    return values
