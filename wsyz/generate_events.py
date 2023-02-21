from datetime import datetime

import pytz
from ics import Event

from wsyz.lectures import lectures_topics, lectures_schedule


def generate_events_wsyz(group='brak'):
    events = set()
    for i, topic in enumerate(lectures_topics):
        event = Event()
        event.name = f'WSYZ Wykład {i+1} - {topic}'
        event.uid = f'23l-wsyz-wyk-{i+1}'
        day_month = lectures_schedule[i]
        event.begin = datetime(2023, day_month[1], day_month[0], 8, 15, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.end = datetime(2023, day_month[1], day_month[0], 10, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.description = 'Sala: 161'
        events.add(event)
    return events
