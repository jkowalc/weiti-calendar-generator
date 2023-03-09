from dataclasses import dataclass

from src.model.calendar_semester import CalendarSemester


@dataclass
class ModelPlan:
    semester: int
    course: str
    calendar_semester: CalendarSemester
    subjects: list

    def __str__(self):
        desc = f"{self.course.upper()} {self.semester} {self.calendar_semester.code}\n"
        for subject in self.subjects:
            desc += f"{subject}\n"
        return desc
