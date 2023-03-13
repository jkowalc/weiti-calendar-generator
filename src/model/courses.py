from enum import Enum

COURSE_SUMMARY_ATTR = {
    'Informatyka': 'EIT',
    'Automatyka i robotyka': 'AIR',
    'Cyberbezpieczeństwo': 'CYB',
    'Elektronika': 'EL',
    'Telekomunikacja': 'TL',
    'Inżynieria internetu rzeczy': 'CYB',
}

COURSE_URLS = {
    'Informatyka': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Informatyka-od-roku-2019-2020-1',
    'Automatyka i robotyka': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Automatyka-i-robotyka-1',
    'Cyberbezpieczeństwo': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Cyberbezpieczenstwo-1',
    'Elektronika': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Elektronika-do-roku-2019-2020-1',
    'Telekomunikacja': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Telekomunikacja-od-roku-2019-2020-1',
    'Inżynieria internetu rzeczy': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Inzynieria-internetu-rzeczy-1',
}


class Course(Enum):
    INF = 'Informatyka'
    AIR = 'Automatyka i robotyka'
    CYB = 'Cyberbezpieczeństwo'
    EL = 'Elektronika'
    TEL = 'Telekomunikacja'
    IIR = 'Inżynieria internetu rzeczy'

    def get_summary_attr(self):
        return COURSE_SUMMARY_ATTR[self.value]

    def get_url(self):
        return COURSE_URLS[self.value]

    def get_max_semesters(course):
        """ For future changes """
        return 7
