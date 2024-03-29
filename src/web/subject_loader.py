from src.model.calendar_semester import CalendarSemester
from src.model.subject import Subject
from src.scrapers.schedule_scraper import scrape_schedule
from src.scrapers.subject_part_scraper import scrape_subject_part
from src.scrapers.subject_scraper import scrape_subject
from src.web.tools import map_multiple_urls, map_single_url
from src.web.tools import retry_if_network_error


def load_subject(url, calendar_semester) -> Subject:
    full_code, simple_code, name, classes_schedule = retry_if_network_error(map_single_url, url,
                                                                            scrape_subject, calendar_semester)
    print("Ładuję przedmiot: ", full_code)
    subject_parts = {}
    subject_parts_info = retry_if_network_error(map_multiple_urls, classes_schedule, scrape_subject_part)
    for class_type, subject_part_info in subject_parts_info.items():
        groups_info = retry_if_network_error(map_multiple_urls, subject_part_info, scrape_schedule)
        filtered_groups_info = {group_code: group_info for group_code, group_info in groups_info.items() if
                                group_info}
        if filtered_groups_info:
            subject_parts[class_type] = filtered_groups_info
    return Subject(full_code, simple_code, name, subject_parts) if subject_parts else None


if __name__ == '__main__':
    print(load_subject('https://usosweb.usos.pw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&kod=103A-INxxx-ISP-SKPS', CalendarSemester('23L')))

