from src.model.semester import Semester


def select_semester():
    current = Semester.get_current()
    inp = input(f"Wybierz semestr (enter - {current.code}): ")
    if inp == '':
        return current
    else:
        return Semester(inp)


if __name__ == '__main__':
    print(select_semester())
