from src.model.subject import Subject
from src.ui.simplify_groups import simplify_groups


def select_group_choice(subject: Subject) -> dict:
    user_choice = {}
    for class_type in subject.classes_schedule:
        groups = list(subject.classes_schedule[class_type].keys())
        if len(groups) > 1:
            print(f"Przedmiot {subject.full_code} ma więcej niż jedną grupę dla typu zajęć {class_type.name}.")
            simplified = simplify_groups(groups)
            group_name = ""
            if not simplified:
                print("Wybierz jedną z poniższych grup:")
                for i, group in enumerate(groups):
                    print(f"{i+1}. {group}")
                group_id = -1
                while group_id not in range(1, len(groups) + 1):
                    group_id = input(f"Wybierz grupę (1 - {len(groups)}): ").strip()
                    group_id = int(group_id) if group_id.isdigit() else -1
                group_name = groups[group_id - 1]
            else:
                inp = ""
                while inp not in range(simplified[0], simplified[1] + 1):
                    inp = input(f"Wybierz jedną z grup {simplified[0]}-{simplified[1]}: ")
                    inp = int(inp) if inp.isdigit() else -1
                group_name = str(inp)
            user_choice[class_type] = group_name
        else:
            print(f"Przedmiot {subject.full_code} ma jedną grupę dla typu zajęć {class_type.name}")
            inp = ""
            while inp not in ['y', 'n']:
                inp = input("Czy chcesz dodać do kalendarza (y/n): ").strip()
            if inp == 'y':
                user_choice[class_type] = groups[0]
    return user_choice


if __name__ == "__main__":
    from src.web.subject_loader import load_subject
    from src.model.calendar_semester import CalendarSemester
    subj = load_subject('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=103A-INxxx-ISP-WSYZ', CalendarSemester('23L'))
    print(select_group_choice(subj))
