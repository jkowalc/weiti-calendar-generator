from src.additional_info.load_info import load_whitelists
from src.additional_info.tools import parse_date, parse_schedule_item
from src.model.calendar_semester import CalendarSemester
from src.model.subject import Subject, ClassType


def filter_schedule(schedule: list, whitelist: list):
    return [item for item in schedule if parse_schedule_item(item) in whitelist]


def group_translation(classes_schedule, translation_dict):
    new_classes_schedule = {}
    for new_group in translation_dict:
        if translation_dict[new_group]:
            new_classes_schedule[new_group] = classes_schedule[translation_dict[new_group]]
        else:
            new_classes_schedule[new_group] = []
    return new_classes_schedule


def filter_conflicts(schedule: list):
    dates = set()
    new_schedule = []
    for item in schedule:
        if parse_schedule_item(item) in dates:
            continue
        dates.add(parse_schedule_item(item))
        new_schedule.append(item)
    return new_schedule


def filter_schedules_for_subject(subject: Subject, whitelists: dict):
    whitelists_for_subject = whitelists.get(subject.full_code)
    if whitelists_for_subject is None:
        return
    for class_type in subject.classes_schedule:
        whitelists_for_class_type = whitelists_for_subject.get(class_type.name)
        if whitelists_for_class_type is None:
            continue
        if isinstance(whitelists_for_class_type, dict) and "group_translation" in whitelists_for_class_type:
            subject.classes_schedule[class_type] = group_translation(subject.classes_schedule[class_type], whitelists_for_class_type["group_translation"])
            del whitelists_for_class_type["group_translation"]
        if len(subject.classes_schedule[class_type]) > 1:
            for group in subject.classes_schedule[class_type]:
                whitelist = whitelists_for_subject[class_type.name].get(group)
                if whitelist is None:
                    continue
                subject.classes_schedule[class_type][group] = filter_schedule(subject.classes_schedule[class_type][group], whitelist)
        else:
            whitelist = whitelists_for_subject.get(class_type.name)
            subject.classes_schedule[class_type][list(subject.classes_schedule[class_type].keys())[0]] = filter_schedule(subject.classes_schedule[class_type][list(subject.classes_schedule[class_type].keys())[0]], whitelist)


if __name__ == "__main__":
    from src.web.subject_loader import load_subject
    subj = load_subject('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=103A-INxxx-ISP-WSYZ', CalendarSemester('23L'))
    whitelists = load_whitelists(CalendarSemester('23L'))
    print(25 * '-' + 'BEFORE' + 25 * '-')
    print(subj)
    filter_schedules_for_subject(subj, whitelists)
    print(25 * '-' + 'AFTER' + 25 * '-')
    print(subj)
