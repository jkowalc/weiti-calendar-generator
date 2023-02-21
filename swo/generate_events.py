from datetime import datetime

import pytz
from ics import Event

from swo.lectures import lectures_schedule, lectures_topics


def generate_events_swo(group='brak'):
    events = set()
    for i, topic in enumerate(lectures_topics):
        event = Event()
        event.name = f'SWO Wykład {i+1} - {topic}'
        event.uid = f'23l-swo-wyk-{i+1}'
        day_month = lectures_schedule[i]
        event.begin = datetime(2023, day_month[1], day_month[0], 10, 15, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.end = datetime(2023, day_month[1], day_month[0], 12, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.description = 'Sala: 161'
        events.add(event)
    return events
