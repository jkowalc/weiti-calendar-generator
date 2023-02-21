from datetime import datetime

import pytz
from ics import Event

from bd2.lectures import lectures_topics, lectures_schedule


def generate_events_bd2():
    events = set()
    for i, topic in enumerate(lectures_topics):
        event = Event()
        event.name = f'BD2 Wykład {i+1} - {topic}'
        event.uid = f'23l-bd2-wyk-{i+1}'
        day_month = lectures_schedule[i]
        event.begin = datetime(2023, day_month[1], day_month[0], 10, 15, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.end = datetime(2023, day_month[1], day_month[0], 12, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.description = 'Sala: 133'
        events.add(event)
    return events
