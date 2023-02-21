from datetime import datetime

import pytz
from ics import Event

from bss.labs import labs_hours, labs_topics, get_labs_schedule
from bss.lectures import lectures_schedule, lectures_topics


def generate_events_bss(group='brak'):
    events = set()
    for i, topic in enumerate(lectures_topics):
        event = Event()
        event.name = f'BSS Wykład {i+1} - {topic}'
        event.uid = f'23l-bss-wyk-{i+1}'
        day_month = lectures_schedule[i]
        event.begin = datetime(2023, day_month[1], day_month[0], 10, 15, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.end = datetime(2023, day_month[1], day_month[0], 12, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.description = f'Sala: 161'
        events.add(event)
    if group != 'brak':
        for i, topic in enumerate(labs_topics):
            event = Event()
            event.name = f'BSS Lab {i+1} - {topic}'
            event.uid = f'23l-bss-lab-{i+1}'
            day_month = get_labs_schedule(group)[i]
            event.begin = datetime(2023, day_month[1], day_month[0], labs_hours[group][0], labs_hours[group][1], 00, tzinfo=pytz.timezone('Europe/Warsaw'))
            event.end = datetime(2023, day_month[1], day_month[0], labs_hours[group][0] + 2, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
            event.description = f'Sala: 139'
            events.add(event)
    return events
