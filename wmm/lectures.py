lectures_schedule = [
    (20, 2),
    (24, 2),
    (27, 2),
    (3, 3),
    (6, 3),
    (10, 3),
    (13, 3),
    (17, 3),
    (20, 3),
    (24, 3),
    (27, 3),
    (31, 3),
    (3, 4),
    (5, 4),
    (14, 4),
    (17, 4),
    (21, 4),
    (24, 4),
    (28, 4),
    (8, 5),
    (15, 5),
    (19, 5),
    (22, 5),
    (26, 5),
    (29, 5),
    (2, 6),
    (5, 6),
    (6, 6),
    (12, 7),
    (16, 6)
]

# Placeholders for the actual topics
lectures_topics = [
    'Sygnały cz. 1',
    'Sygnały cz. 2',
    'Sygnały cz. 3',
    'Sygnały cz. 4',
    'Sygnały cz. 5',
    'Sygnały cz. 6',
    'Wizja cz. 1',
    'Wizja cz. 2',
    'Wizja cz. 3',  # musi być zrobiony obraz
    'Wizja cz. 4',
    'Wizja cz. 5',
    'Wizja cz. 6',
    'Wizja cz. 7',
    'Wizja cz. 8',
    'Dźwięk cz. 1',
    'Dźwięk cz. 2',
    'Dźwięk cz. 3',
    'Dźwięk cz. 4',
    'Dźwięk cz. 5',
    'Dźwięk cz. 6',  # musi być zrobiony dźwięk
    'Dźwięk cz. 7',
    'Grafika cz. 1',
    'Grafika cz. 2',
    'Grafika cz. 3',
    'Termin zapasowy',  # musi być zrobiona grafika
    'Termin zapasowy',
    'Termin zapasowy',
    'Termin zapasowy',
    'Termin zapasowy',
    'Termin zapasowy'
]

if __name__ == '__main__':
    print(len(lectures_schedule))
    print(len(lectures_topics))
    assert len(lectures_schedule) == len(lectures_topics)
