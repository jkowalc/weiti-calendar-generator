import json
import os

from src.model.calendar_semester import CalendarSemester


def load_thing(thing, semester: CalendarSemester):
    things = {}
    files = os.listdir(f"../../config/{thing}/")
    for file in files:
        with open(f"../../config/{thing}/{file}", "r") as f:
            try:
                things_as_json: dict = json.load(f)
            except json.JSONDecodeError:
                raise RuntimeError(f"File {file} is not a valid JSON file.") from None
            if things_as_json.get("semester") == semester.code:
                things_as_json.pop("semester")
                if set(things.keys()).intersection(set(things_as_json.keys())):
                    raise RuntimeError(f"File {file} duplicates key from other file")
                things = things | things_as_json
    return things


def load_whitelists(semester: CalendarSemester):
    return load_thing("schedules", semester)


def load_topics(semester: CalendarSemester):
    return load_thing("topics", semester)


if __name__ == '__main__':
    load_whitelists(CalendarSemester("23L"))
    # print(load_topics(CalendarSemester("23L")))
