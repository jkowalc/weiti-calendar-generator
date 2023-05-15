from ics import Calendar

from src.additional_info.load_info import load_whitelists, load_topics
from src.model.calendar_semester import CalendarSemester
from src.model.user_choice import UserChoice
from src.ui.add_choice_subjects import add_choice_subjects
from src.ui.add_model_plan_subjects import add_model_plan_subjects
from src.ui.add_new_subjects import add_new_subjects
from src.ui.select_semester import select_calendar_semester
from src.ui.save_choice import save_choice, load_choice


def main():
    choice: UserChoice = load_choice()
    cal = Calendar()
    calendar_semester = choice.semester if choice.semester else select_calendar_semester()
    whitelists = load_whitelists(calendar_semester)
    topics = load_topics(calendar_semester)
    if choice:
        add_choice_subjects(cal, calendar_semester, whitelists, topics, choice)
        add_new_subjects(cal, calendar_semester, whitelists, topics, choice)
    else:
        add_model_plan_subjects(cal, calendar_semester, whitelists, topics, choice)
        add_new_subjects(cal, calendar_semester, whitelists, topics, choice)
    choice.semester = calendar_semester
    with open('../calendar.ics', 'w') as fp:
        fp.writelines(cal.serialize_iter())
    save_choice(choice)


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as e:
        print(f"Wystąpił bład: {e}")
