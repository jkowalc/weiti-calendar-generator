from dataclasses import dataclass

from src.model.calendar_semester import CalendarSemester


@dataclass
class ModelPlan:
    semester: int
    course: str
    calendar_semester: CalendarSemester
    subjects: list

