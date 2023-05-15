from src.additional_info.filter_schedule import filter_schedules_for_subject
from src.additional_info.generate_events import generate_events
from src.model.user_choice import UserChoice
from src.ui.select_group_choice import select_group_choice
from src.ui.select_new_subject import select_new_subject
from src.web.subject_loader import load_subject


def add_new_subjects(cal, calendar_semester, whitelists, topics, choice: UserChoice):
    while True:
        inp = input("Czy chcesz dodać kolejny przedmiot? (y/n): ").strip()
        if inp == 'n':
            break
        elif inp == 'y':
            subject_url = select_new_subject()
            subject = load_subject(subject_url, calendar_semester)
            filter_schedules_for_subject(subject, whitelists)
            user_choice = select_group_choice(subject)
            choice.add_subject(subject.full_code, user_choice)
            cal.events = cal.events.union(generate_events(calendar_semester, subject, topics, user_choice))
