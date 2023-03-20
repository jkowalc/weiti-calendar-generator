import re


def parse_subj_input(inp: str):
    inp = inp.strip()
    if inp.startswith('https://') or inp.startswith('http://'):
        return inp
    elif re.match(r'^[A-Z0-9]{4}-[A-Z0-9]{5}-[A-Z0-9]{3}-[A-Z0-9]*$', inp):
        return f'https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod={inp}'
    else:
        return None


def select_new_subject():
    print('Dodawanie nowego przedmiotu')
    inp = None
    while not inp:
        inp = input('Podaj przedmiot (kod lub link): ')
        inp = parse_subj_input(inp)
    return inp


if __name__ == "__main__":
    print(select_new_subject())
