from bs4 import BeautifulSoup, Tag

from src.scrapers.tools import check_if_usos_available, deconstruct_table
from src.model.calendar_semester import CalendarSemester
from src.model.subject import ClassType


def scrape_subject(text, semester: CalendarSemester):
    soup = BeautifulSoup(text, 'html.parser')
    check_if_usos_available(soup)
    description_table = soup.find('usos-frame', {'style': "clear: right; width: fit-content;"}).find('table').find('tbody')
    description = {}
    for row in description_table.find_all('tr'):
        cells = row.find_all('td')
        key = cells[0].text.strip()
        value = cells[1].text.strip()
        description[key] = value
    name = description['Nazwa przedmiotu:']
    full_code = description['Kod przedmiotu:']
    simple_code = None
    if 'Kod wydziałowy:' in description:
        simple_code = description['Kod wydziałowy:']
    elif 'Język prowadzenia:' in description and 'Poziom języka:' in description:
        simple_code = description['Język prowadzenia:'][:3].upper() + ' ' + description['Poziom języka:'][:3]
    classes_schedule = {}
    usos_ui = soup.find('div', {'class': 'usos-ui'})
    for sem in usos_ui.find_all('usos-frame')[1:]:
        title = sem.find('h2', {'slot': 'title'}).text
        title = title[(title.index('\"')+1):]
        title = title[:title.index('\"')]
        if title == semester.get_full_name():
            deconstructed: Tag = deconstruct_table(sem.find('table'))
            for type in deconstructed['Typ zajęć:'].find_all('div', {'style': 'margin: 5px 0;'}):
                type_text = type.text.split(',')[0].strip().upper().replace('Ł', 'L').replace('Ć', 'C').replace('Ś', 'S').replace('Ż', 'Z').replace('Ź', 'Z')
                type_obj = ClassType[type_text]
                url = type.find('a')['href']
                classes_schedule[type_obj] = url
            return full_code, simple_code, name, classes_schedule
    raise Exception('Semestr nie został znaleziony w bazie danych USOS')


if __name__ == '__main__':
    import requests
    text = requests.get('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=103A-INxxx-ISP-WSYZ').text
    print(scrape_subject(text, CalendarSemester('23L')))

