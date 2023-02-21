labs_hours = {
    '101': (18, 15),
    '102': (14, 15),
    '103': (14, 15),
    '104': (12, 15),
    '105': (8, 15),
    '106': (12, 15),
    '107': (16, 15),
    '108': (18, 15),
    '109': (8, 15),
    '110': (16, 15)
}

labs_schedule = {
    'śr': [
        (22, 3),
        (29, 3),
        (12, 4),
        (26, 4),
        (10, 5),
        (17, 5),
        (31, 5),
    ],
    'czw': [
        (23, 3),
        (30, 3),
        (13, 4),
        (27, 4),
        (11, 5),
        (18, 5),
        (1, 6)
    ],
    'wt': [
        (21, 3),
        (28, 3),
        (11, 4),
        (25, 4),
        (9, 5),
        (16, 5),
        (30, 5)
    ]
}

labs_topics = [
    'Algorytmy szyfrowania',
    'OpenSSL',
    'Stunnel',
    'GPG',
    'Systemy IDS',
    'Bezpieczeństwo aplikacji',
    'Bezpieczeństwo aplikacji WWW'
]


def get_labs_schedule(group):
    if group in ['101', '103', '109', '110']:
        return labs_schedule['śr']
    if group in ['102', '105', '106']:
        return labs_schedule['czw']
    if group in ['104', '107', '108']:
        return labs_schedule['wt']
