import json

from src.dev.generate_schedule import generate_schedule
from src.dev.generate_topics import generate_topics
from src.scrapers.model_plan_scraper import get_subjects_for_model_plan
from src.ui.select_model_plan import select_model_plan
from src.ui.select_semester import select_semester


def generate_config():
    model_plan = select_model_plan()
    semester = select_semester()
    subjects = get_subjects_for_model_plan(model_plan, semester)
    schedule = generate_schedule(semester, subjects)
    topics = generate_topics(semester, subjects)
    file_prefix = f"{semester.code}_{model_plan.course}_{model_plan.semester}"
    with open(f"../../config/topics/{file_prefix}_topics.json", "w") as f:
        json.dump(topics, f, indent=4)
    with open(f"../../config/schedules/{file_prefix}_schedule.json", "w") as f:
        json.dump(schedule, f, indent=4)
    print("Plan zajęć i tematy zostały zapisane")


if __name__ == '__main__':
    generate_config()
