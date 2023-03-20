import json

from src.dev.generate_schedule import generate_schedule
from src.dev.generate_topics import generate_topics
from src.model.model_plan import ModelPlan
from src.ui.select_model_plan import select_model_plan
from src.ui.select_semester import select_calendar_semester
from src.web.full_loader import load_model_plan


def generate_config():
    semester, course = select_model_plan()
    calendar_semester = select_calendar_semester()
    model_plan: ModelPlan = load_model_plan(semester, course, calendar_semester)
    schedule = generate_schedule(calendar_semester, model_plan.subjects)
    topics = generate_topics(calendar_semester, model_plan.subjects)
    file_prefix = f"{calendar_semester.code}_{model_plan.course.value}_{model_plan.semester}"
    with open(f"../../config/topics/{file_prefix}_topics_default.json", "w") as f:
        json.dump(topics, f, indent=4)
    with open(f"../../config/schedules/{file_prefix}_schedule_default.json", "w") as f:
        json.dump(schedule, f, indent=4)
    print("\nPlan zajęć i tematy zostały zapisane")


if __name__ == '__main__':
    generate_config()
