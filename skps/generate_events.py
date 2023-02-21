from datetime import datetime

import pytz
from ics import Event

from skps.lectures import lectures_schedule, lectures_topics


def generate_events_skps(group='brak'):
    events = set()
    for i, topic in enumerate(lectures_topics):
        event = Event()
        event.name = f'SKPS Wykład {i+1} - {topic}'
        event.uid = f'23l-skps-wyk-{i+1}'
        day_month = lectures_schedule[i]
        event.begin = datetime(2023, day_month[1], day_month[0], 12, 15, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.end = datetime(2023, day_month[1], day_month[0], 14, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.description = 'Sala: 133'
        events.add(event)
    return events
