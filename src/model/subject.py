import enum
from dataclasses import dataclass
from typing import Dict

SUBJECT_CODE_REGEX = r'^[a-zA-Z0-9]{4}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{3}-[a-zA-Z0-9]*$'


class ClassType(enum.Enum):
    CWICZENIA = "Ćw"
    LABORATORIUM = "Lab"
    PROJEKT = "Proj"
    SEMINARIUM = "Sem"
    WYKLAD = "Wykład"


def schedule_to_str(schedule):
    desc = ''
    for day in schedule:
        desc += f" Start: {day[0]} | Koniec: {day[1]} | Miejsce: {day[2]}\n"
    return desc


@dataclass
class Subject:
    full_code: str
    simple_code: str
    name: str
    classes_schedule: Dict[ClassType, Dict[str, list[tuple]]]

    def __str__(self):
        desc = f"{self.name} ({self.simple_code}) ({self.full_code})\n"
        for type in self.classes_schedule:
            desc += f"------------------------ {type.value} ------------------------\n"
            for group in self.classes_schedule[type]:
                desc += f"Grupa {group}:\n"
                desc += schedule_to_str(self.classes_schedule[type][group])
        return desc
