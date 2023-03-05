import requests
from bs4 import BeautifulSoup, Tag

from src.scrapers.tools import check_if_usos_available, deconstruct_table
from src.scrapers.schedule_scraper import scrape_schedule
from src.model.semester import Semester
from src.model.subject_info import SubjectInfo, ClassType


def scrape_subject_part(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    check_if_usos_available(soup)
    group_table = soup.find_all('table', {'class': 'grey'})[1]
    groups = group_table.find_all('tr')[1:]
    for group in groups:
        if group.get('class') == ['footnote']:
            groups.remove(group)
    if len(groups) == 1:
        cells = groups[0].find_all('td')
        return scrape_schedule(cells[5].find('a')['href'])
    else:
        groups_dict = {}
        for group in groups:
            cells = group.find_all('td')
            group_code = cells[0].text.strip()
            schedule = scrape_schedule(cells[5].find('a')['href'])
            if schedule:
                groups_dict[group_code] = schedule
        return groups_dict


def scrape_subject(url, semester: Semester) -> SubjectInfo:
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
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
    if('Kod wydziałowy:' in description):
        simple_code = description['Kod wydziałowy:']
    elif('Język prowadzenia:' in description and 'Poziom języka:' in description):
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
                type_text = type.text.split(',')[0].strip().upper().replace('Ł', 'L')
                type_obj = ClassType[type_text]
                url = type.find('a')['href']
                subject_part_return = scrape_subject_part(url)
                if subject_part_return:
                    classes_schedule[type_obj] = subject_part_return
            return SubjectInfo(full_code, simple_code, name, classes_schedule)
    raise Exception('Semestr nie został znaleziony w bazie danych USOS')


if __name__ == '__main__':
    subj = scrape_subject('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=103A-INxxx-ISP-WSYZ', Semester('23L'))
    print(subj)
    print(subj.get_version())
