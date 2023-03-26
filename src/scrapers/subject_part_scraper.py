from bs4 import BeautifulSoup

from src.scrapers.tools import check_for_usos_errors


def scrape_subject_part(text):
    soup = BeautifulSoup(text, 'html.parser')
    check_for_usos_errors(soup)
    group_table = soup.find_all('table', {'class': 'grey'})[1]
    groups = group_table.find_all('tr')[1:]
    for group in groups:
        if group.get('class') == ['footnote']:
            groups.remove(group)
    groups_dict = {}
    for group in groups:
        cells = group.find_all('td')
        group_code = cells[0].text.strip()
        groups_dict[group_code] = cells[5].find('a')['href']
    return groups_dict


if __name__ == "__main__":
    import requests
    text = requests.get('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazGrupyZajec&zaj_cyk_id=449897').text
    print(scrape_subject_part(text))
