from src.additional_info.filter_schedule import filter_schedules_for_subject
from src.additional_info.generate_events import generate_events
from src.model.user_choice import UserChoice
from src.ui.select_group_choice import select_group_choice
from src.ui.select_model_plan import select_model_plan
from src.web.full_loader import load_model_plan


def add_model_plan_subjects(cal, calendar_semester, whitelists, topics, choice: UserChoice):
    inp = ""
    while inp not in ['y', 'n']:
        inp = input("Czy chcesz dodać plan modułowy? (y/n): ").strip()
    if inp == 'y':
        semester, course = select_model_plan()
        model_plan = load_model_plan(semester, course, calendar_semester)
        for subject in model_plan.subjects:
            filter_schedules_for_subject(subject, whitelists)
            user_choice = select_group_choice(subject)
            choice.add_subject(subject.full_code, user_choice)
            cal.events = cal.events.union(generate_events(calendar_semester, subject, topics, user_choice))
