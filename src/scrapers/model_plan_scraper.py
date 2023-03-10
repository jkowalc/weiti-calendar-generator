from bs4 import BeautifulSoup
import re

COURSES = {
    'Informatyka': 'EIT',
    'Automatyka i robotyka': 'AIR',
    'Cyberbezpieczeństwo': 'CYB',
    'Elektronika': 'EL',
    'Telekomunikacja': 'TL',
    'Inżynieria internetu rzeczy': 'CYB',
}


def scrape_model_plan(text, course, semester: int):
    """
    :param text: html text of website
    :param course: course name
    :param semester: semester number
    :return: list of subject urls
    """
    subjects = BeautifulSoup(text, 'html.parser') \
        .find(attrs={'summary': COURSES[course]}) \
        .findAll(lambda tag: tag.parent.name != 'i', href=lambda url: url and re.compile("pokazPrzedmiot").search(url))

    return [
        subject['href'] for subject in subjects
        if len(list(x for x in subject.parent.previous_siblings if x.name == 'td')) == semester
    ]


if __name__ == '__main__':
    with open("../../stubs/it_model.html", "r") as fh:
        print(list(scrape_model_plan(fh, 'Informatyka', 1)))
