from datetime import datetime
from typing import List

from src.model.semester import Semester
from src.model.subject_info import SubjectInfo


def parse_schedule(schedule: list):
    return [f"{date[0].day:02}-{date[0].month:02}" for date in schedule]


def generate_schedule_for_subject(subject: SubjectInfo):
    return_dict = {}
    for class_type in subject.classes_schedule:
        if isinstance(subject.classes_schedule[class_type], dict):
            return_dict[class_type.value] = {}
            for group in subject.classes_schedule[class_type]:
                return_dict[class_type.value][group] = parse_schedule(subject.classes_schedule[class_type][group])
        else:
            return_dict[class_type.value] = parse_schedule(subject.classes_schedule[class_type])
    return return_dict


def generate_schedule(semester: Semester, subjects: List[SubjectInfo]):
    schedule = {'semester': semester.code}
    for subject in subjects:
        schedule[subject.full_code] = generate_schedule_for_subject(subject)
    return schedule
