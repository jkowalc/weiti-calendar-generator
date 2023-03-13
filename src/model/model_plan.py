from dataclasses import dataclass

from src.model.calendar_semester import CalendarSemester
from src.model.courses import Course


@dataclass
class ModelPlan:
    semester: int
    course: Course
    calendar_semester: CalendarSemester
    subjects: list

    def __str__(self):
        desc = f"{self.course.value.upper()} {self.semester} {self.calendar_semester.code}\n"
        for subject in self.subjects:
            desc += f"{subject}\n"
        return desc
