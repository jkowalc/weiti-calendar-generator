import dataclasses

from src.model.calendar_semester import CalendarSemester
from src.model.subject import ClassType


class UserChoice:
    semester: CalendarSemester
    subjects: dict[str, dict[ClassType, str]]

    def __init__(self, semester=None, subjects=None):
        self.semester = semester
        self.subjects = subjects if subjects else {}

    def serialize(self):
        serialized = {'semester': self.semester.code, 'subjects': {}}
        for subj in self.subjects:
            serialized['subjects'][subj] = {}
            for class_type in self.subjects[subj]:
                serialized['subjects'][subj][class_type.value] = self.subjects[subj][class_type]
        return serialized

    @staticmethod
    def from_deserialized(deserialized):
        new_subjects = {}
        deserialized_subjects = deserialized['subjects']
        for subj in deserialized_subjects:
            new_subjects[subj] = {}
            for class_type_str in deserialized_subjects[subj]:
                new_subjects[subj][ClassType(class_type_str)] = deserialized_subjects[subj][class_type_str]
        return UserChoice(CalendarSemester(deserialized['semester']), new_subjects)

    def add_subject(self, subject, choice):
        if subject in self.subjects:
            pass  # maybe raise error?
        self.subjects[subject] = choice

    def has_subjects(self):
        return len(self.subjects) > 0
