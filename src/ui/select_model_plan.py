from typing import Tuple

from src.model.courses import Course


def select_model_plan() -> Tuple[int, Course]:
    courses = [course for course in Course]
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course.value}")
    course = courses[int(input("Wybierz kierunek: ")) - 1]
    max_semesters = course.get_max_semesters()
    semester = 0
    while semester not in range(1, max_semesters + 1):
        semester = int(input(f"Wybierz który semestr (1-{max_semesters}): "))
    return semester, course
