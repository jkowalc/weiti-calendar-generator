from typing import List

from src.additional_info.tools import parse_schedule_item
from src.model.calendar_semester import CalendarSemester
from src.model.subject import Subject


def parse_schedule(schedule: list):
    return [parse_schedule_item(date) for date in schedule]


def generate_schedule_for_subject(subject: Subject):
    return_dict = {}
    for class_type in subject.classes_schedule:
        if len(subject.classes_schedule[class_type]) > 1:
            return_dict[class_type.name] = {}
            for group in subject.classes_schedule[class_type]:
                return_dict[class_type.name][group] = parse_schedule(subject.classes_schedule[class_type][group])
        else:
            return_dict[class_type.name] = parse_schedule(subject.classes_schedule[class_type][list(subject.classes_schedule[class_type].keys())[0]])
    return return_dict


def generate_schedule(semester: CalendarSemester, subjects: List[Subject]):
    schedule = {'semester': semester.code}
    for subject in subjects:
        schedule[subject.full_code] = generate_schedule_for_subject(subject)
    return schedule
