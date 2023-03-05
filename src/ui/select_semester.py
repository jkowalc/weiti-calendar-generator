from src.model.semester import Semester


def select_semester() -> Semester:
    current = Semester.get_current()
    inp = 'input'
    while inp != '' and not (inp[-1] in ['Z', 'L'] and inp[:-1].isdigit()):
        inp = input(f"Wybierz semestr (enter - {current.code}): ")
    if inp == '':
        return current
    else:
        return Semester(inp)


if __name__ == '__main__':
    print(select_semester())
