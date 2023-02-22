from datetime import datetime

from bs4 import BeautifulSoup, Tag
import requests
import pytz


def time_data_to_datetime(time_data):
    date_split = time_data[0].split('-')
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])
    time_split = time_data[1].split(':')
    time_split = [obj.strip() for obj in time_split]
    hour_begin = int(time_split[0])
    minute_begin = int(time_split[1])
    hour_end = int(time_split[2])
    minute_end = int(time_split[3])
    return datetime(year, month, day, hour_begin, minute_begin, tzinfo=pytz.timezone('Europe/Warsaw')), \
        datetime(year, month, day, hour_end, minute_end, tzinfo=pytz.timezone('Europe/Warsaw'))


def scrape_schedule(url):
    events = []
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    tbody = soup.find('table', id='lista_dat_spotkan').find('tbody')
    for row in tbody.find_all('tr'):
        time: Tag = row.find('td')
        time_data = []
        for child in time.children:
            text = child.text.strip()
            if text:
                time_data.append(text)
        begin, end = time_data_to_datetime(time_data)
        events.append((begin, end, time_data[2].capitalize()))
    events.sort(key=lambda x: x[0])
    return events


if __name__ == '__main__':
    events = scrape_schedule('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazZajecia&zaj_cyk_id=449968&gr_nr=1')
    for event in events:
        print(event)
