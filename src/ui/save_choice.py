import json
from pathlib import Path

from src.model.user_choice import UserChoice

SAVE_PATH = Path(".user_choice")


def save_choice(choice: UserChoice):
    choice = choice.serialize()
    try:
        with open(SAVE_PATH, mode="w") as f:
            json.dump(choice, f)
    except TypeError:
        print("Save failed")


def load_choice() -> UserChoice:
    try:
        with open(SAVE_PATH, mode="r") as f:
            print("Znaleziono zapisany ostatni wybór.")
            inp = ''
            while inp not in ['y', 'n']:
                inp = input("Czy chcesz załadować? (y/n): ").strip()
            if inp == 'y':
                return UserChoice.from_deserialized(json.load(f))
            else:
                return UserChoice()
    except FileNotFoundError:
        return UserChoice()
    except KeyError:
        raise RuntimeError('.user_choice file corrupted')
