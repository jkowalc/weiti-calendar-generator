from ics import Calendar

from src.additional_info.filter_schedule import filter_schedules_for_subject
from src.additional_info.generate_events import generate_events
from src.additional_info.load_info import load_whitelists, load_topics
from src.ui.select_group_choice import select_group_choice
from src.ui.select_model_plan import select_model_plan
from src.ui.select_new_subject import select_new_subject
from src.ui.select_semester import select_calendar_semester
from src.web.full_loader import load_model_plan
from src.web.subject_loader import load_subject


def main():
    cal = Calendar()
    calendar_semester = select_calendar_semester()
    whitelists = load_whitelists(calendar_semester)
    topics = load_topics(calendar_semester)
    inp = ""
    while inp not in ['y', 'n']:
        inp = input("Czy chcesz dodać plan modułowy? (y/n): ").strip()
    if inp == 'y':
        semester, course = select_model_plan()
        model_plan = load_model_plan(semester, course, calendar_semester)
        for subject in model_plan.subjects:
            filter_schedules_for_subject(subject, whitelists)
            user_choice = select_group_choice(subject)
            cal.events = cal.events.union(generate_events(calendar_semester, subject, topics, user_choice))
    while True:
        inp = input("Czy chcesz dodać kolejny przedmiot? (y/n): ").strip()
        if inp == 'n':
            break
        elif inp == 'y':
            subject_url = select_new_subject()
            subject = load_subject(subject_url, calendar_semester)
            filter_schedules_for_subject(subject, whitelists)
            user_choice = select_group_choice(subject)
            cal.events = cal.events.union(generate_events(calendar_semester, subject, topics, user_choice))
    with open('../calendar.ics', 'w') as fp:
        fp.writelines(cal.serialize_iter())
    pass


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as e:
        print(f"Wystąpił bład: {e}")
