from ics import Event

from src.model.calendar_semester import CalendarSemester
from src.model.subject import Subject, ClassType

EXAM_PREFIXES = ['Kol', 'Kolokwium']


def is_exam(topic):
    for prefix in EXAM_PREFIXES:
        if topic.startswith(prefix):
            return True
    return False


def generate_events(calendar_semester: CalendarSemester, subject: Subject, topics, user_choice):
    topics = topics.get(subject.full_code)
    events = set()
    for class_type in subject.classes_schedule:
        topics_per_class = topics.get(class_type.name) if topics is not None else None
        choice = user_choice.get(class_type)
        if choice is None:
            continue
        standard_count, exam_count = 0, 0
        for i, schedule_item in enumerate(subject.classes_schedule[class_type][choice]):
            topics_per_group = topics_per_class.get(choice) if topics_per_class is not None else None
            topic: str = topics_per_group.get(i+1) if topics_per_group is not None else None
            event = Event()
            name = f"{subject.simple_code}"
            if topic is not None and is_exam(topic):
                name += f" Kol {exam_count+1} "
                exam_count += 1
            elif topic is not None:
                name += f" {class_type.value} {standard_count+1} - {topic} "
                standard_count += 1
            else:
                name += f" {class_type.value} {standard_count+1}"
                standard_count += 1
            event.name = name
            event.uid = f"{calendar_semester.code}-{subject.full_code}-{class_type.value}-{i+1}"
            event.begin = schedule_item[0]
            event.end = schedule_item[1]
            event.description = schedule_item[2]
            events.add(event)
    return events


if __name__ == "__main__":
    from src.web.subject_loader import load_subject
    subj = load_subject('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=103A-INxxx-ISP-WSYZ', CalendarSemester('23L'))
    events = generate_events(CalendarSemester('23L'), subj, {}, {
        ClassType.LABORATORIUM: '101'
    })
    print(list(events)[0])
