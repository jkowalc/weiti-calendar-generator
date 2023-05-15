import json
from pathlib import Path

from src.model.subject import ClassType

SAVE_PATH = Path(".user_choice")


def serialize_choice(choice):
    new_choice = {'semester': choice['semester'], 'subjects': {}}
    for subj in choice['subjects']:
        new_choice['subjects'][subj] = {}
        for class_type in choice['subjects'][subj]:
            new_choice['subjects'][subj][class_type.value] = choice['subjects'][subj][class_type]
    return new_choice


def deserialize_choice(choice):
    new_choice = {'semester': choice['semester'], 'subjects': {}}
    for subj in choice['subjects']:
        new_choice['subjects'][subj] = {}
        for class_type_str in choice['subjects'][subj]:
            new_choice['subjects'][subj][ClassType(class_type_str)] = choice['subjects'][subj][class_type_str]
    return new_choice


def save_choice(choice):
    choice = serialize_choice(choice)
    try:
        with open(SAVE_PATH, mode="w") as f:
            json.dump(choice, f)
    except TypeError:
        print("Save failed")


def load_choice():
    try:
        with open(SAVE_PATH, mode="r") as f:
            print("Znaleziono zapisany ostatni wybór.")
            inp = ''
            while inp not in ['y', 'n']:
                inp = input("Czy chcesz załadować? (y/n): ").strip()
            if inp == 'y':
                return deserialize_choice(json.load(f))
            else:
                return {}
    except FileNotFoundError:
        return {}
    except KeyError:
        raise RuntimeError('.user_choice file corrupted')
