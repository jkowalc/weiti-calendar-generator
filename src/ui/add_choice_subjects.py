import re

from src.additional_info.filter_schedule import filter_schedules_for_subject
from src.additional_info.generate_events import generate_events
from src.model.subject import SUBJECT_CODE_REGEX
from src.model.user_choice import UserChoice
from src.web.subject_loader import load_subject


def parse_subject_code(inp):
    if re.match(SUBJECT_CODE_REGEX, inp):
        return f'https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod={inp}'
    else:
        raise RuntimeError('.user_choice file corrupted')


def add_choice_subjects(cal, calendar_semester, whitelists, topics, choice: UserChoice):
    for subject_code in choice.subjects:
        url = parse_subject_code(subject_code)
        subject = load_subject(url, calendar_semester)
        filter_schedules_for_subject(subject, whitelists)
        user_choice = choice.subjects[subject_code]
        choice.add_subject(subject.full_code, user_choice)
        cal.events = cal.events.union(generate_events(calendar_semester, subject, topics, user_choice))
