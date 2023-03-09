from src.model.calendar_semester import CalendarSemester


def select_calendar_semester() -> CalendarSemester:
    current = CalendarSemester.get_current()
    inp = 'input'
    while inp != '' and not (inp[-1] in ['Z', 'L'] and inp[:-1].isdigit()):
        inp = input(f"Wybierz semestr (enter - {current.code}): ")
    if inp == '':
        return current
    else:
        return CalendarSemester(inp)


if __name__ == '__main__':
    print(select_calendar_semester())
