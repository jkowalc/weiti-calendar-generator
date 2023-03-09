from dataclasses import dataclass


@dataclass
class ModelPlan:
    semester: int
    course: str
    subjects: list

