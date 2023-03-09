from bs4 import Tag


def check_if_usos_available(soup):
    if soup.find('title').text.strip() == 'USOSweb tymczasowo niedostępny - USOSWEB PW':
        raise RuntimeError('USOS jest aktualnie niedostępny (przerwa techniczna)')


def deconstruct_table(table: Tag):
    values = {}
    tbody = table.find('tbody')
    for row in tbody.find_all('tr'):
        cells = row.find_all('td')
        key = cells[0].text.strip()
        value = cells[1]
        values[key] = value
    return values


def schedule_to_str(schedule):
    desc = ''
    for day in schedule:
        desc += f" Start: {day[0]} | Koniec: {day[1]} | Miejsce: {day[2]}\n"
    return desc

