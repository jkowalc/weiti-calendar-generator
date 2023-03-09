import enum
from dataclasses import dataclass
from typing import Any, Dict


class ClassType(enum.Enum):
    CWICZENIA = "Ćw"
    LABORATORIUM = "Lab"
    PROJEKT = "Proj"
    SEMINARIUM = "Sem"
    WYKLAD = "Wykład"

@dataclass
class Subject:
    full_code: str
    simple_code: str
    name: str
    classes_schedule: Dict[ClassType, Dict[str, list[tuple]]]

    # def __str__(self):
    #     desc = f"{self.name} ({self.simple_code}) ({self.full_code})\n"
    #     for type in self.classes_schedule:
    #         desc += f"-------------- {type.value} --------------\n"
    #         if isinstance(self.classes_schedule[type], dict):
    #             for group in self.classes_schedule[type]:
    #                 desc += f"Grupa {group}:\n"
    #                 desc += schedule_to_str(self.classes_schedule[type][group])
    #         else:
    #             desc += schedule_to_str(self.classes_schedule[type])
    #     return desc


