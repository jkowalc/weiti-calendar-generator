from src.model.calendar_semester import CalendarSemester
from src.model.courses import Course
from src.model.model_plan import ModelPlan
from src.model.subject import Subject
from src.scrapers.model_plan_scraper import scrape_model_plan
from src.scrapers.schedule_scraper import scrape_schedule
from src.scrapers.subject_part_scraper import scrape_subject_part
from src.scrapers.subject_scraper import scrape_subject
from src.web.tools import map_multiple_urls, map_single_url


def load_model_plan(semester: int, course: Course, calendar_semester: CalendarSemester) -> ModelPlan:
    """
    :param semester: semester number
    :param course: course name
    :param calendar_semester: calendar semester
    :return: list of subject urls
    """
    plan_url = course.get_url()
    subjects_urls = map_single_url(plan_url, scrape_model_plan, course, semester)
    subjects_info = map_multiple_urls(subjects_urls, scrape_subject, calendar_semester)
    subjects = []
    for full_code, simple_code, name, classes_schedule in subjects_info:
        subject_parts = {}
        subject_parts_info = map_multiple_urls(classes_schedule, scrape_subject_part)
        for class_type, subject_part_info in subject_parts_info.items():
            groups_info = map_multiple_urls(subject_part_info, scrape_schedule)
            filtered_groups_info = {group_code: group_info for group_code, group_info in groups_info.items() if
                                    group_info}
            if filtered_groups_info:
                subject_parts[class_type] = filtered_groups_info
        if subject_parts:
            subjects.append(Subject(full_code, simple_code, name, subject_parts))
            print(".", end="")
    return ModelPlan(semester, course, calendar_semester, subjects)


if __name__ == '__main__':
    print(load_model_plan(4, Course.INF, CalendarSemester('23L')))
