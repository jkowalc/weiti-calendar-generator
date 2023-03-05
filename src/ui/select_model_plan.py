from src.model.model_plan_info import ModelPlanInfo

courses = [
    "Automatyka i Robotyka",
    "Cyberbezpieczeństwo",
    "Elektronika",
    "Elektronika (od 2020)",
    "Informatyka",
    "Informatyka (od 2019)",
    "Inżynieria biomedyczna",
    "Inżynieria biomedyczna (od 2018)",
    "Inżynieria internetu rzeczy",
    "Telekomunikacja",
    "Telekomunikacja (od 2019)",
]


def get_max_semesters(course):
    """ For future changes """
    return 7


def select_model_plan() -> ModelPlanInfo:
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course}")
    course = courses[int(input("Wybierz kierunek: ")) - 1]
    max_semesters = get_max_semesters(course)
    semester = 0
    while semester not in range(1, max_semesters + 1):
        semester = int(input(f"Wybierz który semestr (1-{max_semesters}): "))
    return ModelPlanInfo(semester, course)
