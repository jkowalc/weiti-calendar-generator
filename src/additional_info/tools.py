import datetime


def parse_date(date: datetime):
    return f"{date.day:02}-{date.month:02}"


def parse_schedule_item(item):
    assert parse_date(item[0]) == parse_date(item[1])
    return parse_date(item[0])
