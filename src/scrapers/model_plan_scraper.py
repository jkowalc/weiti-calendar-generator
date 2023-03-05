from src.model.model_plan_info import ModelPlanInfo
from src.scrapers.subject_scraper import scrape_subject


def scrape_model_plan(model_plan_info: ModelPlanInfo):
    """
    :param model_plan_info:
    :return: list of subject urls
    """
    return [
        "https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=103B-INxxx-ISP-BSS",
        "https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=103A-INxxx-ISP-SWO"
    ]


def get_subjects_for_model_plan(model_plan, semester):
    return [scrape_subject(url, semester) for url in scrape_model_plan(model_plan)]
