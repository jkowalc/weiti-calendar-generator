from datetime import datetime

import pytz
from ics import Event

from wmm.labs import labs_topics, labs_schedule, labs_hours, labs_places
from wmm.lectures import lectures_schedule, lectures_topics


def generate_events_wmm(group='brak'):
    events = set()
    for i, topic in enumerate(lectures_topics):
        event = Event()
        event.name = f'WMM Wykład {i+1} - {topic}'
        event.uid = f'23l-wmm-wyk-{i+1}'
        day_month = lectures_schedule[i]
        date = datetime(2023, day_month[1], day_month[0], 12, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        if date.isoweekday() == 1:
            event.description = 'Sala: 161'
            event.begin = datetime(2023, day_month[1], day_month[0], 14, 15, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
            event.end = datetime(2023, day_month[1], day_month[0], 16, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        else:
            event.description = 'Sala: 133'
            event.begin = datetime(2023, day_month[1], day_month[0], 10, 15, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
            event.end = datetime(2023, day_month[1], day_month[0], 12, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        events.add(event)
    for i, topic in enumerate(labs_topics):
        event = Event()
        event.name = f'WMM Lab {i+1} - {topic}'
        event.uid = f'23l-wmm-lab-{i+1}'
        day_month = labs_schedule[group][i]
        event.begin = datetime(2023, day_month[1], day_month[0], labs_hours[group][0], labs_hours[group][1], 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.end = datetime(2023, day_month[1], day_month[0], labs_hours[group][0] + 3, 00, 00, tzinfo=pytz.timezone('Europe/Warsaw'))
        event.description = f'Sala: {labs_places[group]}'
        events.add(event)
    return events
